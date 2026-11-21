// Measures each concept page's full height at desktop (1440) and phone (390) for the canvas frames.
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const dir = __dirname + '/pages-out/';
  const pages = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== 'index.html');
  const b = await chromium.launch();
  const out = {};
  for (const w of [1440, 390]) {
    const p = await b.newPage({viewport: {width: w, height: 900}});
    for (const f of pages) {
      await p.goto('file://' + dir + f, {waitUntil: 'load'});
      await p.waitForTimeout(150);
      const h = await p.evaluate(() => Math.ceil(document.documentElement.scrollHeight));
      (out[f] = out[f] || {})[w] = h;
    }
  }
  await b.close();
  fs.writeFileSync(__dirname + '/heights.json', JSON.stringify(out, null, 1));
  console.log(Object.keys(out).length, 'pages measured');
})();
