/* GENERATED FILE - DO NOT EDIT. Copied from storefront/main.js by tools/sync_docs.py. Edit storefront/main.js and re-run the script; edits made here are overwritten. */
/* ==========================================================================
   TI-84 Plus CE Python Study Toolkit — landing page behaviour.
   Vanilla JS, no dependencies. Everything degrades gracefully without it:
   the nav links, the pricing table and the FAQ all work with JS disabled.
   ========================================================================== */
(function () {
  'use strict';

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

    // Reset the menu state when the layout grows back past the mobile breakpoint.
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

  /* ---- free-pack signup form ----
     Inert on purpose until it is pointed at a real endpoint. Rather than
     silently doing nothing (or worse, looking like it worked), it tells the
     visitor to use the buy link. Once you set a real form action or swap in a
     Gumroad link, delete this handler. See SETUP_CHECKLIST.md. */
  var form = document.getElementById('signupForm');
  var status = document.getElementById('formStatus');

  if (form && status) {
    form.addEventListener('submit', function (e) {
      var action = form.getAttribute('action');
      var wired = action && action !== '#' && action !== '';
      if (wired) return; // real endpoint configured — let the browser submit

      e.preventDefault();
      var email = form.querySelector('input[type="email"]');
      var value = email ? email.value.trim() : '';

      if (!value || value.indexOf('@') < 1 || value.lastIndexOf('.') < value.indexOf('@')) {
        status.textContent = 'Please enter a valid email address.';
        status.classList.add('is-error');
        if (email) email.focus();
        return;
      }

      status.classList.remove('is-error');
      status.textContent =
        'Signup is not connected yet — the free pack download link goes here. ' +
        'Site owner: wire this form up per SETUP_CHECKLIST.md.';
    });
  }

  /* ---- placeholder buy links ----
     Every purchase link is marked with class="js-buy". Until real store URLs
     are pasted in, clicking one would jump to the top of the page and look
     broken, so intercept it and say so plainly. This whole block can be
     deleted once the hrefs are real. */
  document.querySelectorAll('a.js-buy').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');
      if (!href || href === '#') {
        e.preventDefault();
        window.alert(
          'Checkout link not configured yet.\n\n' +
          'Site owner: replace href="#" on this button with your Gumroad or Etsy ' +
          'product URL. Each one is marked with a "BUY LINK" comment in index.html.'
        );
      }
    });
  });
})();
