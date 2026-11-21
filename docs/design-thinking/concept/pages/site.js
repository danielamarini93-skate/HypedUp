/* Hyped Up key pages concept: menu sheet, builds filter, quote form, footer wordmark. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  /* phone menu */
  var sheet = $('#sheet');
  $$('[data-menu]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.dataset.menu === 'open';
      sheet.hidden = !open; document.body.style.overflow = open ? 'hidden' : '';
      (open ? $('[data-menu="close"]') : $('[data-menu="open"]')).focus();
    });
  });

  /* desktop dropdowns */
  var dds = $$('.dd>button');
  dds.forEach(function (b) { b.addEventListener('click', function (e) { e.stopPropagation(); var open = b.getAttribute('aria-expanded') !== 'true';
    dds.forEach(function (x) { x.setAttribute('aria-expanded', 'false'); document.getElementById(x.getAttribute('aria-controls')).hidden = true; });
    if (open) { b.setAttribute('aria-expanded', 'true'); document.getElementById(b.getAttribute('aria-controls')).hidden = false; } }); });
  document.addEventListener('click', function () { dds.forEach(function (x) { x.setAttribute('aria-expanded', 'false'); document.getElementById(x.getAttribute('aria-controls')).hidden = true; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') document.body.click(); });
  /* phone menu doors (accordion) */
  var doors = $$('.sheet .doors>li>button');
  doors.forEach(function (b) { b.addEventListener('click', function () { var open = b.getAttribute('aria-expanded') !== 'true';
    doors.forEach(function (x) { x.setAttribute('aria-expanded', 'false'); document.getElementById(x.getAttribute('aria-controls')).hidden = true; });
    if (open) { b.setAttribute('aria-expanded', 'true'); document.getElementById(b.getAttribute('aria-controls')).hidden = false; } }); });
  /* footer columns: open on desktop, collapsed on phones */
  var mq = matchMedia('(min-width:1000px)');

  // footer columns are plain lists now (no accordion)

  /* homepage B: service finder tabs */
  var ft = $$('[data-ftab]');
  ft.forEach(function (b) { b.addEventListener('click', function () { ft.forEach(function (x) { x.setAttribute('aria-selected', x === b ? 'true' : 'false'); });
    $$('[data-fpanel]').forEach(function (p) { p.hidden = p.dataset.fpanel !== b.dataset.ftab; }); }); });
  /* blog category filter */
  $$('[data-blogcat]').forEach(function (b) { b.addEventListener('click', function () { var c = b.dataset.blogcat;
    $$('[data-blogcat]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    $$('.postgrid li').forEach(function (li) { li.hidden = !(c === 'All' || li.dataset.cat === c); }); }); });

  /* service pages: "Pick your setup" tabs (click + arrow keys) */
  $$('[data-picker]').forEach(function (pk) {
    var tabs = $$('[role=tab]', pk);
    function sel(t, focus) { tabs.forEach(function (x) { var on = x === t; x.setAttribute('aria-selected', on ? 'true' : 'false'); x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).hidden = !on; }); if (focus) t.focus(); t.scrollIntoView({block: 'nearest', inline: 'nearest'}); }
    tabs.forEach(function (t, i) { t.addEventListener('click', function () { sel(t); });
      t.addEventListener('keydown', function (e) { var k = e.key, n = null;
        if (k === 'ArrowRight' || k === 'ArrowDown') n = tabs[(i + 1) % tabs.length]; if (k === 'ArrowLeft' || k === 'ArrowUp') n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (n) { e.preventDefault(); sel(n, true); } }); });
  });

  /* footer wordmark: fit the outlined SVG text to its own box */
  function fitWm() { $$('.wmsvg').forEach(function (sv) { var b = sv.querySelector('text').getBBox(), p = 4; sv.setAttribute('viewBox', (b.x - p) + ' ' + (b.y - p) + ' ' + (b.width + p * 2) + ' ' + (b.height + p * 2)); }); }
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(fitWm); fitWm();


  /* builds filter */
  $$('[data-filter]').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.dataset.filter;
      $$('[data-filter]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $$('.gal figure').forEach(function (fig) { fig.hidden = !(f === 'all' || (fig.dataset.tags || '').indexOf(f) > -1); });
    });
  });

  /* quote form */
  var form = $('#quote');
  if (form) {
    var qs = new URLSearchParams(location.search);
    qs.getAll('service').join(',').split(',').forEach(function (v) { var x = v && form.querySelector('input[name="need"][value="' + v + '"]'); if (x) x.checked = true; });
    if (qs.get('car') && form.elements.vehicle) form.elements.vehicle.value = qs.get('car');
    var val = function (n) { var e = form.elements[n]; return e ? e.value.trim() : ''; };
    var text = function () {
      var need = $$('input[name="need"]:checked', form).map(function (x) { return x.dataset.label; });
      return 'Hi Hypa, I\'d like a quote.\n' +
        'For: ' + (need.join(', ') || '…') + '\n' +
        'Car: ' + (val('vehicle') || '…') + '\n' +
        val('more');
    };
    var eb = $('#by-email'), box = $('#emailbox');
    eb.addEventListener('click', function () { box.hidden = false; eb.setAttribute('aria-expanded', 'true'); $('#name').focus(); });
    var ph = $('#photos');
    ph.addEventListener('change', function () { var n = ph.files.length; $('#ph-label').textContent = n ? n + (n > 1 ? ' photos added' : ' photo added') : 'Add photos'; });
    $$('[data-src] button').forEach(function (b) { b.addEventListener('click', function () { $$('[data-src] button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); }); });
    var out = $('#sent'), msg = $('#sent-msg'), prev = $('#sent-preview');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var via = e.submitter && e.submitter.value;
      if (via === 'email') {
        var bad = null;
        [['name', function (v) { return v.length > 1; }], ['email', function (v) { return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v); }]].forEach(function (f) {
          var el = form.elements[f[0]], ok = f[1](el.value.trim());
          el.setAttribute('aria-invalid', ok ? 'false' : 'true'); $('#' + f[0] + '-err').hidden = ok;
          if (!ok && !bad) bad = el;
        });
        if (bad) { bad.focus(); return; }
      }
      out.hidden = false; form.hidden = true;
      if (via === 'whatsapp') {
        msg.textContent = 'WhatsApp would open now with this message written. Nothing is sent until you press send.';
        prev.hidden = false; prev.textContent = text();
      } else {
        msg.textContent = 'Got it, thanks. Hypa replies by email, usually within [reply time TBC] on working days.';
        prev.hidden = true;
      }
      out.focus();
    });
    var back = $('#sent-back');
    if (back) back.addEventListener('click', function () { out.hidden = true; form.hidden = false; });
  }
  /* video loops: play only on screen, pause button, respect reduced motion */
  var rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var vids = $$('.media video');
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { var v = e.target; if (v.dataset.user === 'paused') return; if (e.isIntersecting) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } else v.pause(); });
  }, { threshold: 0.25 }) : null;
  vids.forEach(function (v) {
    var b = v.parentNode.querySelector('.vpause');
    var sync = function () { if (!b) return; b.setAttribute('aria-label', v.paused ? 'Play video' : 'Pause video'); b.classList.toggle('is-paused', v.paused); };
    if (rm) { v.removeAttribute('autoplay'); v.pause(); v.dataset.user = 'paused'; }
    else if (io) io.observe(v);
    v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
    if (b) b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation();
      if (v.paused) { v.dataset.user = ''; v.play(); } else { v.dataset.user = 'paused'; v.pause(); } });
  });
})();
