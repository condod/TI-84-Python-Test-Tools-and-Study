/* GENERATED FILE - DO NOT EDIT. Copied from storefront/main.js by tools/sync_docs.py. Edit storefront/main.js and re-run the script; edits made here are overwritten. */
/* ==========================================================================
   TI-84 Plus CE Python Study Toolkit — landing page behaviour.
   Renders the 156-program catalog and talks to the local Stripe/email demo
   server (python storefront/serve.py). Without API keys, buy/email explain
   that they are waiting rather than failing silently.
   ========================================================================== */
(function () {
  'use strict';

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function priceLabel(n) {
    return n ? '$' + n : 'Free';
  }

  function buyBtn(sku, label, extraClass) {
    extraClass = extraClass || 'btn-outline';
    if (sku === 'free') {
      return '<a class="btn ' + extraClass + ' js-buy" href="#free" data-sku="free">' + esc(label) + '</a>';
    }
    return '<a class="btn ' + extraClass + ' js-buy" href="#buy" data-sku="' + esc(sku) + '">' + esc(label) + '</a>';
  }

  function renderCatalog() {
    var cat = window.TI84_CATALOG;
    if (!cat) return;

    var rows = document.getElementById('bundleRows');
    if (rows) {
      var html = '';
      var free = cat.free;
      html += '<tr><th scope="row"><span class="tbl-name">' + esc(free.name) +
        '</span><span class="tbl-sub">' + esc(free.short) + '</span></th>' +
        '<td>' + free.programs.length + '</td><td>' + esc(free.best) + '</td>' +
        '<td class="price-cell"><span class="price">Free</span></td>' +
        '<td>' + buyBtn('free', 'Get it free') + '</td></tr>';
      cat.bundles.forEach(function (b) {
        html += '<tr><th scope="row"><span class="tbl-name">' + esc(b.name) +
          '</span><span class="tbl-sub">' + esc(b.short) + '</span></th>' +
          '<td>' + b.programs.length + '</td><td>' + esc(b.best) + '</td>' +
          '<td class="price-cell"><span class="price">' + priceLabel(b.price) + '</span></td>' +
          '<td>' + buyBtn(b.sku, 'Buy') + '</td></tr>';
      });
      var c = cat.complete;
      html += '<tr class="row-featured"><th scope="row"><span class="tbl-name">' +
        esc(c.name) + ' <span class="tag tag-best">Best value</span></span>' +
        '<span class="tbl-sub">' + esc(c.short) + '</span></th>' +
        '<td>' + c.count + '</td><td>' + esc(c.best) + '</td>' +
        '<td class="price-cell"><span class="price">$' + c.price +
        '</span><span class="price-was">$' + cat.separateTotal + ' separately</span></td>' +
        '<td>' + buyBtn('complete', 'Buy the toolkit', 'btn-primary') + '</td></tr>';
      rows.innerHTML = html;
    }

    var cards = document.getElementById('priceCards');
    if (cards) {
      var ch = '';
      function card(name, price, meta, desc, sku, featured) {
        ch += '<article class="price-card' + (featured ? ' pc-featured' : '') + '">' +
          '<h3>' + name + (featured ? ' <span class="tag tag-best">Best value</span>' : '') + '</h3>' +
          '<p class="pc-price">' + price + '</p>' +
          '<p class="pc-meta">' + meta + '</p>' +
          '<p class="pc-desc">' + desc + '</p>' +
          buyBtn(sku, sku === 'free' ? 'Get it free' : (sku === 'complete' ? 'Buy the toolkit' : 'Buy'),
            (sku === 'complete' ? 'btn-primary' : 'btn-outline') + ' btn-block') +
          '</article>';
      }
      card(esc(cat.free.name), 'Free', cat.free.programs.length + ' programs · any course',
        esc(cat.free.short), 'free', false);
      cat.bundles.forEach(function (b) {
        card(esc(b.name), '$' + b.price, b.programs.length + ' programs · ' + esc(b.best),
          esc(b.short), b.sku, false);
      });
      card(esc(cat.complete.name), '$' + cat.complete.price +
        ' <span class="pc-was">$' + cat.separateTotal + ' separately</span>',
        'All ' + cat.complete.count + ' programs · every subject',
        'The entire library: study toolkit, companion packs, and arcade.',
        'complete', true);
      cards.innerHTML = ch;
    }

    var grid = document.getElementById('includeGrid');
    if (grid) {
      var gh = '';
      cat.bundles.forEach(function (b) {
        gh += '<article class="card include-card"><header class="include-head"><h3>' +
          esc(b.name) + '</h3><span class="pill">' + b.programs.length +
          ' programs · $' + b.price + '</span></header><ul class="prog-list">';
        b.programs.forEach(function (p) {
          var extra = p.oncalc ? ' <code>' + esc(p.oncalc) + '</code>' : '';
          gh += '<li><code>' + esc(p.file) + '</code>' + extra +
            '<span>' + esc(p.blurb) + '</span></li>';
        });
        gh += '</ul></article>';
      });
      grid.innerHTML = gh;
    }
  }

  /* ---- mobile navigation ---- */
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('primaryNav');

  if (toggle && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 760) setOpen(false);
    });
  }

  /* ---- header shadow once the page scrolls ---- */
  var header = document.getElementById('siteHeader');
  if (header) {
    var syncHeader = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    syncHeader();
    window.addEventListener('scroll', syncHeader, { passive: true });
  }

  renderCatalog();

  /* ---- API status (Stripe + email keys) ---- */
  var banner = document.getElementById('demoBanner');
  var apiStatus = { stripe: false, email: false, demo: true };

  function showBanner(show) {
    if (!banner) return;
    if (show) banner.removeAttribute('hidden');
    else banner.setAttribute('hidden', '');
  }

  fetch('/api/status')
    .then(function (r) { return r.json(); })
    .then(function (s) {
      apiStatus = s;
      showBanner(!(s.stripe && s.email));
    })
    .catch(function () {
      showBanner(true);
    });

  function findBundle(sku) {
    var cat = window.TI84_CATALOG;
    if (!cat) return null;
    if (sku === 'free') return cat.free;
    if (sku === 'complete') return cat.complete;
    for (var i = 0; i < cat.bundles.length; i++) {
      if (cat.bundles[i].sku === sku) return cat.bundles[i];
    }
    return null;
  }

  function waitingMessage() {
    return 'Checkout is waiting for your Stripe and email API keys. ' +
      'Paste STRIPE_SECRET_KEY and RESEND_API_KEY into storefront/.env, ' +
      'then restart python storefront/serve.py.';
  }

  document.addEventListener('click', function (e) {
    var link = e.target.closest && e.target.closest('a.js-buy');
    if (!link) return;
    var sku = link.getAttribute('data-sku');
    if (!sku || sku === 'free') return; // free pack uses #free form
    e.preventDefault();
    if (!apiStatus.stripe) {
      window.alert(waitingMessage());
      return;
    }
    link.classList.add('is-busy');
    fetch('/api/checkout', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sku: sku })
    })
      .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (res.j && res.j.url) {
          window.location = res.j.url;
          return;
        }
        window.alert(res.j && res.j.error ? res.j.error : waitingMessage());
      })
      .catch(function () {
        window.alert(waitingMessage());
      })
      .finally(function () {
        link.classList.remove('is-busy');
      });
  });

  /* ---- free-pack signup ---- */
  var form = document.getElementById('signupForm');
  var status = document.getElementById('formStatus');

  if (form && status) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.querySelector('input[type="email"]');
      var value = email ? email.value.trim() : '';
      if (!value || value.indexOf('@') < 1 || value.lastIndexOf('.') < value.indexOf('@')) {
        status.textContent = 'Please enter a valid email address.';
        status.classList.add('is-error');
        status.classList.remove('is-ok');
        if (email) email.focus();
        return;
      }
      if (!apiStatus.email) {
        status.classList.add('is-error');
        status.classList.remove('is-ok');
        status.textContent = waitingMessage();
        return;
      }
      status.classList.remove('is-error');
      status.textContent = 'Sending…';
      fetch('/api/free-pack', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: value })
      })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && res.j && res.j.ok) {
            status.classList.remove('is-error');
            status.classList.add('is-ok');
            status.textContent = 'Sent — check your inbox for the free starter pack.';
            return;
          }
          status.classList.add('is-error');
          status.classList.remove('is-ok');
          status.textContent = (res.j && res.j.error) || waitingMessage();
        })
        .catch(function () {
          status.classList.add('is-error');
          status.textContent = waitingMessage();
        });
    });
  }
})();
