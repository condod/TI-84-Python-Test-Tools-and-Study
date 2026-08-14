#!/usr/bin/env python3
"""Local demo server for the TI-84 storefront.

Serves the static landing page and, once keys are in ``.env``:

* POST /api/checkout  — Stripe Checkout Session (secret key never sent to the browser)
* POST /api/free-pack — emails the free starter pack via Resend
* GET  /api/status    — which keys are present (booleans only)

Usage::

    copy storefront\\.env.example storefront\\.env
    # paste STRIPE_SECRET_KEY and RESEND_API_KEY
    python storefront/serve.py

Then open http://127.0.0.1:8765/
"""
from __future__ import annotations

import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PORT = int(os.environ.get("PORT", "8765"))


def load_env(path: str) -> dict[str, str]:
    env: dict[str, str] = {}
    if not os.path.isfile(path):
        return env
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


ENV = load_env(os.path.join(HERE, ".env"))
STRIPE_SECRET = ENV.get("STRIPE_SECRET_KEY") or os.environ.get("STRIPE_SECRET_KEY", "")
RESEND_KEY = ENV.get("RESEND_API_KEY") or os.environ.get("RESEND_API_KEY", "")
EMAIL_FROM = ENV.get("EMAIL_FROM") or os.environ.get(
    "EMAIL_FROM", "TI-84 Python <noreply@example.com>"
)
PUBLIC_BASE = ENV.get("PUBLIC_BASE") or os.environ.get(
    "PUBLIC_BASE", f"http://127.0.0.1:{PORT}"
)


def catalog() -> dict:
    path = os.path.join(HERE, "catalog.js")
    raw = open(path, encoding="utf-8").read()
    raw = raw.split("window.TI84_CATALOG =", 1)[1].strip()
    if raw.endswith(";"):
        raw = raw[:-1]
    return json.loads(raw)


def find_product(sku: str) -> dict | None:
    cat = catalog()
    if sku == "free":
        return cat["free"]
    if sku == "complete":
        return cat["complete"]
    for b in cat["bundles"]:
        if b["sku"] == sku:
            return b
    return None


def stripe_checkout(sku: str) -> dict:
    if not STRIPE_SECRET:
        return {"error": "Waiting for STRIPE_SECRET_KEY in storefront/.env"}
    prod = find_product(sku)
    if prod is None or sku == "free":
        return {"error": "Unknown product"}
    price = int(prod.get("price") or 0)
    if price <= 0:
        return {"error": "That pack is free — use the email form."}
    name = prod.get("name") or sku
    data = {
        "mode": "payment",
        "success_url": PUBLIC_BASE + "/?paid=1&sku=" + urllib.parse.quote(sku),
        "cancel_url": PUBLIC_BASE + "/#bundles",
        "line_items[0][quantity]": "1",
        "line_items[0][price_data][currency]": "usd",
        "line_items[0][price_data][unit_amount]": str(price * 100),
        "line_items[0][price_data][product_data][name]": "TI-84 Python — " + name,
        "metadata[sku]": sku,
    }
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(
        "https://api.stripe.com/v1/checkout/sessions",
        data=body,
        method="POST",
        headers={
            "Authorization": "Bearer " + STRIPE_SECRET,
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            out = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        return {"error": "Stripe error: " + detail[:400]}
    url = out.get("url")
    if not url:
        return {"error": "Stripe did not return a checkout URL"}
    return {"url": url}


def send_free_pack(email: str) -> dict:
    if not RESEND_KEY:
        return {"error": "Waiting for RESEND_API_KEY in storefront/.env"}
    if "@" not in email or "." not in email.split("@")[-1]:
        return {"error": "Please enter a valid email address."}
    html = """<p>Here is the free TI-84 Plus CE Python starter pack (5 programs):</p>
<ul>
<li>unit_converter.py</li>
<li>quadratic_solver.py</li>
<li>descriptive_stats.py</li>
<li>unit_circle_reference.py</li>
<li>shape_geometry_solver.py</li>
</ul>
<p>Download the ZIP from the public toolkit:
<a href="https://github.com/condod/TI-84-Python-Test-Tools-and-Study">github.com/condod/TI-84-Python-Test-Tools-and-Study</a>
(the free starter files live in the subject folders listed on the site).</p>
<p>These are study aids. Check your own exam's calculator policy.</p>"""
    payload = json.dumps(
        {
            "from": EMAIL_FROM,
            "to": [email],
            "subject": "Your free TI-84 Python starter pack",
            "html": html,
        }
    ).encode()
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        method="POST",
        headers={
            "Authorization": "Bearer " + RESEND_KEY,
            "Content-Type": "application/json",
        },
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        return {"error": "Email error: " + detail[:400]}
    return {"ok": True}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def _json(self, code: int, obj: dict) -> None:
        raw = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _read_json(self) -> dict:
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0:
            return {}
        return json.loads(self.rfile.read(n).decode() or "{}")

    def do_GET(self) -> None:
        if self.path.split("?", 1)[0] == "/api/status":
            self._json(
                200,
                {
                    "stripe": bool(STRIPE_SECRET),
                    "email": bool(RESEND_KEY),
                    "demo": True,
                },
            )
            return
        if self.path.split("?", 1)[0] in ("/", "/index.html"):
            self.path = "/index.html"
        super().do_GET()

    def do_POST(self) -> None:
        path = self.path.split("?", 1)[0]
        try:
            body = self._read_json()
        except json.JSONDecodeError:
            self._json(400, {"error": "Invalid JSON"})
            return
        if path == "/api/checkout":
            sku = str(body.get("sku") or "")
            out = stripe_checkout(sku)
            self._json(200 if "url" in out else 400, out)
            return
        if path == "/api/free-pack":
            email = str(body.get("email") or "").strip()
            out = send_free_pack(email)
            self._json(200 if out.get("ok") else 400, out)
            return
        self._json(404, {"error": "Unknown API path"})

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("demo: " + (fmt % args) + "\n")


def main() -> None:
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print("TI-84 storefront demo: http://127.0.0.1:%s/" % PORT)
    if STRIPE_SECRET:
        print("Stripe key: loaded")
    else:
        print("Stripe key: WAITING — paste STRIPE_SECRET_KEY into storefront/.env")
    if RESEND_KEY:
        print("Email key:  loaded")
    else:
        print("Email key:  WAITING — paste RESEND_API_KEY into storefront/.env")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
