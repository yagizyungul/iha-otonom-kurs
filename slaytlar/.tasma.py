#!/usr/bin/env python3
"""Slayt taşma dedektörü.

İKİ KEZ YANILDI, ikisinin de dersi burada:

  1) Eşik çok yüksekti (30). Kod paneli #f2eefc, sayfa zemini #f6f7f9 —
     aradaki fark 16. Panel "arka plan" sayılıp eleniyordu, slayt 12'deki
     apt komutu altbilgiye binmesine rağmen temiz göründü. Eşik 10.

  2) Altbilgi çizgisi TAMAMEN örtülünce "çizgi bulunamadı" deyip kontrolü
     atlıyordu — yani en kötü durumda susuyordu. Artık çizginin y konumu
     bütün slaytlardan ortak olarak belirleniyor ve o satır her slaytta
     zorla kontrol ediliyor.

Kullanım:  python3 .tasma.py bolum-02-export
"""
import glob, re, sys
import numpy as np
from PIL import Image

ZEMIN = np.array((246, 247, 249))
CIZGI = np.array((221, 225, 232))     # --ky-cizgi, altbilgi üst çizgisi
ESIK  = 10                            # kod panelini (fark 16) yakalar

def sayi(p): return int(re.search(r'(\d+)\.png$', p).group(1))
def yukle(p): return np.asarray(Image.open(p).convert('RGB')).astype(int)

def cizgi_satiri(dosyalar):
    """Altbilgi çizgisinin y konumu — slaytların ÇOĞUNLUĞUNDAN öğrenilir.
    Tek slayda bakıp öğrenmek riskli: o slayt taşan slayt olabilir."""
    oylar = {}
    for f in dosyalar:
        a = yukle(f); h, w, _ = a.shape
        benzer = (np.abs(a - CIZGI).sum(axis=2) < 24)
        alt = benzer[int(h*0.85):, :]
        sayim = alt.sum(axis=1)
        if sayim.max() > w * 0.5:
            y = int(h*0.85) + int(sayim.argmax())
            oylar[y] = oylar.get(y, 0) + 1
    if not oylar:
        return None
    return max(oylar.items(), key=lambda kv: kv[1])[0]

def main():
    dizin = sys.argv[1] if len(sys.argv) > 1 else 'bolum-02-export'
    dosyalar = sorted(glob.glob(f'{dizin}/*.png'), key=sayi)
    if not dosyalar:
        print(f'{dizin} içinde PNG yok'); return 1

    y = cizgi_satiri(dosyalar)
    if y is None:
        print('UYARI: altbilgi çizgisi hiçbir slaytta bulunamadı')

    sorunlu = []
    for f in dosyalar:
        a = yukle(f); h, w, _ = a.shape
        disi = np.abs(a - ZEMIN).sum(axis=2) > ESIK
        neden = []

        # 1) kenara değen içerik
        for ad, bolge in (('alt', disi[h-4:h, :]),
                          ('sağ', disi[:, w-4:w]),
                          ('üst', disi[0:4, :])):
            if bolge.sum() > 20:
                neden.append(f'{ad} kenara değiyor ({int(bolge.sum())} px)')

        # 2) altbilgi çizgisinin ALTINA taşan içerik
        #    Çizginin kırılmasına bakmak İŞE YARAMIYOR: altbilgi içeriğin
        #    ÜSTÜNE çiziliyor, panel taşsa bile çizgi bozulmadan duruyor.
        #    Doğru ölçüt, çizginin altındaki satırlarda geniş içerik aramak.
        #    Ölçüm: temiz slaytta en yoğun satır ~300 px (marka yazısı),
        #    taşanda 1768 px (tam genişlik panel). Eşik 400.
        if y is not None:
            alt = disi[y+6:h-2]
            satir = alt.sum(axis=1)
            if satir.max() > 400:
                tasma = int((satir > 400).sum() / 1.96)   # tuval birimi
                neden.append(f'altbilgiye taşıyor (~{tasma} px)')

        if neden:
            sorunlu.append((sayi(f), '; '.join(neden)))

    print(f'{len(dosyalar)} slayt · altbilgi çizgisi y={y}\n')
    if not sorunlu:
        print('  Taşma yok ✓')
    else:
        for n, s in sorunlu:
            print(f'  slayt {n:>3}  {s}')
        print(f'\n  toplam {len(sorunlu)} slayt')
    return 0

if __name__ == '__main__':
    sys.exit(main())
