/**
 * Slayt taşma denetçisi.
 *
 *   node tasma-denetle.mjs [http://localhost:3030] [slayt-sayisi]
 *
 * Neden gerekli: içerik alt marka şeridinin altına taştığında dışa aktarımda
 * SESSİZCE kesiliyor — PNG'ye bakmadan fark edilmiyor. 260 slaytta her birini
 * gözle kontrol etmek mümkün değil.
 *
 * Piksel sayma denemesi yanlış alarm veriyordu (alt satırdaki normal metni
 * taşma sanıyordu). Bu yüzden tarayıcıya soruyoruz: slaydın içeriği kendi
 * kutusundan uzun mu (scrollHeight > clientHeight), ve herhangi bir öğe
 * şeridin üstünü geçiyor mu.
 *
 * DİKKAT: Slidev DOM'da aynı anda ÜÇ slayt tutuyor (önceki / şimdiki /
 * sonraki). querySelector('.slidev-layout') bunlardan ilkini — yani
 * görünmeyen, genişliği 0 olan öncekini — döndürüyordu; ölçüm yanlış
 * slayttan alındığı için taşan slaytlar "temiz" raporlanıyordu.
 * Görünür slayt, genişliği 0'dan büyük olandır.
 */
import { chromium } from 'playwright-chromium'

const KOK = process.argv[2] || 'http://localhost:3030'
const N = Number(process.argv[3] || 14)

const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1280, height: 720 } })

let sorunlu = 0
for (let i = 1; i <= N; i++) {
  await p.goto(`${KOK}/${i}`, { waitUntil: 'networkidle' })
  await p.evaluate(() => document.fonts.ready)
  await p.waitForTimeout(320)

  const r = await p.evaluate(() => {
    const k = [...document.querySelectorAll('.slidev-layout')]
      .find(e => e.getBoundingClientRect().width > 0)
    if (!k) return null
    const serit = document.querySelector('.ky-altbilgi')
    const sk = k.getBoundingClientRect()
    const ss = serit ? serit.getBoundingClientRect() : null
    // Şeridin üst kenarını geçen en alttaki metin öğesini bul
    let enAlt = 0, suclu = ''
    for (const e of k.querySelectorAll('p, li, h1, h2, h3, pre, figcaption, .ky-kutu')) {
      const rc = e.getBoundingClientRect()
      if (rc.height === 0) continue
      if (rc.bottom > enAlt) { enAlt = rc.bottom; suclu = (e.textContent || '').trim().slice(0, 42) }
    }
    return {
      kaydirma: k.scrollHeight - k.clientHeight,
      tasma: ss ? Math.round(enAlt - ss.top) : 0,
      suclu,
    }
  })

  if (!r) { console.log(`  ${String(i).padStart(2)}  okunamadi`); continue }
  const kotu = r.kaydirma > 2 || r.tasma > 0
  if (kotu) sorunlu++
  const durum = kotu
    ? `TASMA  serit ustunu ${r.tasma}px geciyor  ->  "${r.suclu}…"`
    : 'temiz'
  console.log(`  ${String(i).padStart(2)}  ${durum}`)
}

console.log(sorunlu === 0
  ? `\n  ${N} slaytin hepsi temiz.`
  : `\n  ${sorunlu} slaytta tasma var — icerigi kisalt ya da ikiye bol.`)

await b.close()
process.exit(sorunlu === 0 ? 0 : 1)
