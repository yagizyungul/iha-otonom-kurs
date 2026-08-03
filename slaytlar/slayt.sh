#!/bin/bash
# Bölüm slaytları için tek giriş noktası.
#
#   ./slayt.sh 00            → tarayıcıda aç (canlı önizleme)
#   ./slayt.sh 00 png        → bolum-00-export/ içine PNG bas
#   ./slayt.sh 00 pdf        → bolum-00.pdf
#   ./slayt.sh 00 denetle    → taşma denetimi (önce ./slayt.sh 00 çalışıyor olmalı)
#
# Neden script: her bölüm ayrı .md dosyası, npm script'ine dosya adı
# gömülürse her bölümde package.json değiştirmek gerekiyor.
set -euo pipefail
cd "$(dirname "$0")"

BOLUM="${1:?Kullanım: ./slayt.sh <bolum-no> [png|pdf|denetle]}"
ISLEM="${2:-dev}"
KAYNAK="bolum-${BOLUM}.md"

[ -f "$KAYNAK" ] || { echo "HATA: $KAYNAK yok."; exit 1; }

case "$ISLEM" in
  dev)
    npx slidev "$KAYNAK" --open
    ;;
  png)
    rm -rf "bolum-${BOLUM}-export"
    npx slidev export "$KAYNAK" --format png --output "bolum-${BOLUM}-export"
    echo ">>> bolum-${BOLUM}-export/ hazır."
    ;;
  pdf)
    npx slidev export "$KAYNAK" --format pdf --output "bolum-${BOLUM}.pdf"
    echo ">>> bolum-${BOLUM}.pdf hazır."
    ;;
  denetle)
    # Slayt sayısı = '---' ayraç sayısı - 1
    # (dosya başındaki frontmatter iki ayraç harcıyor, aralarındaki her
    #  ayraç bir slayt sınırı: 14 ayraç -> 13 slayt)
    N=$(( $(grep -c '^---$' "$KAYNAK") - 1 ))
    node tasma-denetle.mjs http://localhost:3030 "$N"
    ;;
  *)
    echo "Bilinmeyen işlem: $ISLEM  (dev|png|pdf|denetle)"; exit 1
    ;;
esac
