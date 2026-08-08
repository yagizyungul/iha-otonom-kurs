import { chromium } from 'playwright-chromium'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1740, height: 1376 } })
await p.goto(`http://localhost:3030/${process.argv[2] || '13'}`, { waitUntil: 'networkidle' })
await p.evaluate(() => document.fonts.ready)
await p.waitForTimeout(1800)
await p.screenshot({ path: process.argv[3] || '/tmp/canli.png' })
await b.close()
