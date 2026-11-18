(function () {
  'use strict';

  var nav = document.querySelector('.nav');
  var hero = document.querySelector('.hero');

  // Header turns solid once the hero has scrolled away
  if (nav && hero && 'IntersectionObserver' in window) {
    var sentinel = document.createElement('div');
    sentinel.setAttribute('aria-hidden', 'true');
    sentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:' + Math.round(window.innerHeight * 0.6) + 'px;pointer-events:none';
    hero.appendChild(sentinel);
    new IntersectionObserver(function (entries) {
      nav.classList.toggle('is-solid', !entries[0].isIntersecting);
    }).observe(sentinel);
  }

  // Mobile menu
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('menu');
  if (toggle && menu) {
    var icon = toggle.querySelector('use');
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      icon.setAttribute('href', 'assets/icons.svg#i-' + (open ? 'x' : 'list'));
      menu.hidden = !open;
      menu.classList.toggle('is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
      nav.classList.toggle('is-solid', open || window.scrollY > window.innerHeight * 0.6);
    };
    toggle.addEventListener('click', function () { setOpen(menu.hidden); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) { setOpen(false); toggle.focus(); }
    });
    window.matchMedia('(min-width: 961px)').addEventListener('change', function (m) { if (m.matches) setOpen(false); });
  }

  // Events: each one hides itself once its date has passed; if none are left, show the Facebook note
  document.querySelectorAll('.events').forEach(function (list) {
    var shown = [];
    list.querySelectorAll('.event[data-until]').forEach(function (ev) {
      var until = new Date(ev.getAttribute('data-until'));
      if (!isNaN(until) && Date.now() > until.getTime()) ev.hidden = true;
      else shown.push(ev);
    });
    var later = list.querySelector('.event--later');
    if (!shown.length && later) { later.hidden = false; shown.push(later); }
    if (shown.length) shown[0].classList.add('is-first');
  });

  // Rate tabs (WAI-ARIA tabs pattern with arrow-key support)
  document.querySelectorAll('[data-tabs]').forEach(function (box) {
    var tabs = Array.prototype.slice.call(box.querySelectorAll('[role="tab"]'));
    var select = function (tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
      if (focus) tab.focus();
    };
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab, false); });
      tab.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
        else if (e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
        else if (e.key === 'Home') n = tabs[0];
        else if (e.key === 'End') n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); select(n, true); }
      });
    });
  });

  // Year in footer
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Booking form: compose a WhatsApp message
  var form = document.getElementById('book-form');
  if (form) {
    var date = form.querySelector('#f-date');
    var today = new Date();
    var pad = function (n) { return (n < 10 ? '0' : '') + n; };
    date.min = today.getFullYear() + '-' + pad(today.getMonth() + 1) + '-' + pad(today.getDate());

    var check = function (input) {
      var err = document.getElementById(input.id + '-err');
      var ok = input.value.trim() !== '';
      input.setAttribute('aria-invalid', ok ? 'false' : 'true');
      if (ok) input.removeAttribute('aria-describedby'); else input.setAttribute('aria-describedby', err.id);
      err.hidden = ok;
      return ok;
    };
    ['f-name', 'f-date'].forEach(function (id) {
      var el = document.getElementById(id);
      el.addEventListener('blur', function () { if (el.getAttribute('aria-invalid')) check(el); });
      el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') check(el); });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('#f-name');
      var okName = check(name);
      var okDate = check(date);
      if (!okName || !okDate) { (okName ? date : name).focus(); return; }

      var d = new Date(date.value + 'T12:00:00');
      var pretty = d.toLocaleDateString('en-ZA', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
      var extras = Array.prototype.map.call(form.querySelectorAll('input[name="extra"]:checked'), function (c) { return c.value; });
      var note = form.querySelector('#f-note').value.trim();

      var lines = [
        'Hi Malelane Golf Club, I would like to book a tee time.',
        '',
        'Name: ' + name.value.trim(),
        'Date: ' + pretty,
        'Players: ' + form.querySelector('#f-players').value,
        'Round: ' + form.querySelector('#f-round').value
      ];
      if (extras.length) lines.push('Also interested in: ' + extras.join(' and '));
      if (note) lines.push('', note);

      window.open('https://wa.me/27604857945?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
  }
})();
