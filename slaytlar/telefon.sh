#!/bin/bash
# Slaytları telefonda okumak için — müfredat GÜN 0 ADIM 7 "bugünün slayt testi"
#
# Kullanım:  ./telefon.sh 00          (bölüm 00'ı dışa aktarır + yayınlar)
#            ./telefon.sh 00 -hizli   (mevcut PNG'leri yayınlar, yeniden aktarmaz)
#
# Telefon ve bilgisayar AYNI Wi-Fi'da olmalı. Buluta bir şey yüklenmiyor.
set -euo pipefail
cd "$(dirname "$0")"

PORT=8080
BOLUM="${1:?Kullanım: ./telefon.sh <bolum-no>  (ör. ./telefon.sh 00)}"
KAYNAK="bolum-${BOLUM}.md"
DIZIN="bolum-${BOLUM}-export"

[ -f "$KAYNAK" ] || { echo "HATA: $KAYNAK yok."; exit 1; }

if [ "${2:-}" != "-hizli" ]; then
    echo ">>> PNG'ler üretiliyor ($KAYNAK)..."
    rm -rf "$DIZIN"
    npx slidev export "$KAYNAK" --format png --output "$DIZIN" >/dev/null 2>&1
fi

SAYI=$(ls "$DIZIN"/*.png 2>/dev/null | wc -l)
[ "$SAYI" -gt 0 ] || { echo "HATA: $DIZIN içinde PNG yok."; exit 1; }

# Telefonda kaydırarak okunacak basit bir sayfa. Zemin koyu ki açık
# slaytların kenarı belli olsun ve gerçek boyut algısı bozulmasın.
{
cat <<'HTML'
<!doctype html><html lang="tr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Slayt testi</title>
<style>
  :root { color-scheme: dark; }
  body { margin:0; background:#101319; color:#c9d1de;
         font:16px/1.5 system-ui,-apple-system,sans-serif; }
  header { padding:14px 16px; border-bottom:1px solid #262c38; }
  header b { color:#fff; }
  main { padding:12px; display:flex; flex-direction:column; gap:22px; }
  figure { margin:0; }
  img { width:100%; height:auto; display:block; border-radius:6px; }
  figcaption { padding:6px 2px 0; font-size:13px; color:#7c8798; }
  footer { padding:18px 16px 40px; font-size:13px; color:#7c8798; }
</style></head><body>
<header><b>Slayt testi</b> — okuyamadığın yazı varsa not al</header><main>
HTML
echo "<!-- $KAYNAK -->"
i=0
for f in $(ls "$DIZIN"/*.png | sort -V); do
    i=$((i+1))
    echo "<figure><img src=\"$f\" alt=\"Slayt $i\" loading=\"lazy\"><figcaption>Slayt $i</figcaption></figure>"
done
cat <<'HTML'
</main>
<footer>Yakınlaştırmadan oku. Zorlanıyorsan tema/stil.css içindeki
--ky-metin / --ky-kod değerleri büyütülecek demektir.</footer>
</body></html>
HTML
} > telefon.html

IP=$(ip -4 -o addr show scope global 2>/dev/null | grep -v docker | awk 'NR==1{split($4,a,"/"); print a[1]}')

echo
echo "  ================================================"
echo "   Telefonun tarayıcısında şunu aç:"
echo
echo "        http://$IP:$PORT/telefon.html"
echo
echo "   ($SAYI slayt · aynı Wi-Fi'da olmalısın)"
echo "   Durdurmak için: Ctrl+C"
echo "  ================================================"
echo

python3 -m http.server "$PORT" --bind 0.0.0.0
