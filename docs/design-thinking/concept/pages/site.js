/* Hyped Up key pages concept: menu sheet, "Style it." morph, builds filter, quote form, footer wordmark. */
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

  /* footer wordmark: fit the outlined SVG text to its own box */
  function fitWm() { $$('.wmsvg').forEach(function (sv) { var b = sv.querySelector('text').getBBox(), p = 4; sv.setAttribute('viewBox', (b.x - p) + ' ' + (b.y - p) + ' ' + (b.width + p * 2) + ' ' + (b.height + p * 2)); }); }
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(fitWm); fitWm();

  /* "Style it." morph: one font at a time, 3 loops, rests on Graffiti City; static with reduced motion */
  var el = $('#morph');
  if (el) {
    var F = { graffiti: ['"Graffiti City"', 1, 400, 0, 0], serif: ['"Instrument Serif"', 1.12, 400, 1, 0], caps: ['"Big Shoulders Display"', 1.02, 900, 0, 1] };
    var chars = [];
    el.textContent = '';
    'Style it.'.split('').forEach(function (c) { var s = document.createElement('span'); s.className = 'ch'; s.setAttribute('aria-hidden', 'true'); s.dataset.c = c; el.appendChild(s); chars.push(s); });
    el.classList.add('js');
    var apply = function (s, k) { var f = F[k]; s.style.fontFamily = f[0] + ',sans-serif'; s.style.fontSize = f[1] + 'em'; s.style.fontWeight = f[2]; s.style.fontStyle = f[3] ? 'italic' : 'normal'; var c = s.dataset.c; s.textContent = c === ' ' ? ' ' : (f[4] ? c.toUpperCase() : c); };
    var paint = function () { var W = el.offsetWidth; chars.forEach(function (s) { s.style.backgroundSize = (W + 40) + 'px 100%'; s.style.backgroundPosition = (-s.offsetLeft) + 'px 0'; }); };
    chars.forEach(function (s) { apply(s, 'graffiti'); }); paint();
    if (document.fonts) document.fonts.ready.then(paint);
    addEventListener('resize', paint);
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
      var seq = ['serif', 'caps', 'graffiti'], i = 0;
      var round = function () {
        var step = seq[i % seq.length]; i++;
        chars.forEach(function (s) { s.classList.add('sw'); });
        setTimeout(function () { chars.forEach(function (s) { apply(s, step); s.classList.remove('sw'); }); paint(); }, 160);
        if (i < seq.length * 3) setTimeout(round, step === 'graffiti' ? 2600 : 1500);
      };
      setTimeout(round, 1800);
    }
  }

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
    var svc = new URLSearchParams(location.search).get('service');
    if (svc) { var box = form.querySelector('input[value="' + svc + '"]'); if (box) box.checked = true; }
    var val = function (n) { var e = form.elements[n]; return e ? e.value.trim() : ''; };
    var text = function () {
      var need = $$('input[name="need"]:checked', form).map(function (x) { return x.dataset.label; });
      return 'Hi Hypa, I\'d like a quote.\n' +
        'For: ' + (need.join(', ') || '…') + '\n' +
        'Vehicle: ' + (val('vehicle') || '…') + (val('reg') ? ' (' + val('reg') + ')' : '') + '\n' +
        (val('more') ? val('more') + '\n' : '') +
        'Name: ' + (val('name') || '…');
    };
    var out = $('#sent'), msg = $('#sent-msg'), prev = $('#sent-preview');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var via = e.submitter && e.submitter.value;
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
})();
