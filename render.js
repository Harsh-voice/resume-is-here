const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + __dirname + '/film.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const total = await p.evaluate(() => window.TOTAL_FRAMES);
  const FPS = 30;
  const t0 = Date.now();
  for (let i = 0; i < total; i++) {
    await p.evaluate(t => window.render(t), i / FPS);
    await p.screenshot({
      path: __dirname + '/frames/f' + String(i).padStart(5, '0') + '.jpg',
      type: 'jpeg', quality: 92
    });
    if (i % 150 === 0) {
      const el = (Date.now() - t0) / 1000;
      console.log(`  ${i}/${total}  ${el.toFixed(0)}s elapsed`);
    }
  }
  console.log(`done ${total} frames in ${((Date.now()-t0)/1000).toFixed(0)}s`);
  if (errs.length) console.log('PAGE ERRORS:', errs);
  await b.close();
})();
