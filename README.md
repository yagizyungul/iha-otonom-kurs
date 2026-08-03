# ArduPilot + Gazebo ile Otonom İHA Simülasyonu

Bu depo, **ArduPilot + Gazebo ile Otonom İHA Simülasyonu** kursunun kod,
slayt ve kurulum materyallerini içerir.

Kurs, Ubuntu kurulumundan başlayıp 3 uçaklı bir Gazebo/ArduPilot SITL
simülasyonunun kurulmasına, Python (pymavlink) ile otonom uçuş kontrolüne,
kamera akışının işlenmesine ve çok bilgisayarlı yarışma senaryosuna kadar
gider. Gerçek uçuş kartı, model uçak veya saha gerekmez.

---

## Gereksinimler

| | |
|---|---|
| İşletim sistemi | Ubuntu 22.04 LTS |
| RAM | En az 8 GB (16 GB önerilir) |
| Disk | 40 GB boş alan |
| Ekran kartı | Ayrık ekran kartı önerilir (Gazebo 3D) |
| Python | 3.10+ |

---

## Kurulum

Kurulum adımlarının tamamı kursun **Bölüm 2**'sinde anlatılıyor.
Script'ler `kurulum/` klasöründe:

```bash
git clone https://github.com/yagizyungul/iha-otonom-kurs.git
cd iha-otonom-kurs/kurulum
```

Kurulum sırası:

1. ArduPilot (kaynaktan derleme)
2. Gazebo Harmonic
3. `ardupilot_gazebo` plugin'i
4. SITL modelleri ve ortam değişkenleri

> Her adımın karşılığı olan ders numarası script'lerin başında yazıyor.

---

## Klasör yapısı

```
iha-otonom-kurs/
├── kurulum/     kurulum script'leri (Bölüm 2)
├── kod/         bölüm bölüm Python kodları
├── gorevler/    .waypoints görev dosyaları
├── slaytlar/    ders slaytları (Slidev kaynağı)
└── ODEVLER.md   bölüm sonu ödevleri
```

---

## Sürüm notları

ArduPilot ve Gazebo sık güncelleniyor. Kurstaki komutlarla kendi
sisteminde gördüğün çıktı farklıysa `SURUM_NOTLARI.md` dosyasına bak.

## Destek

Sorularını kursun **Soru-Cevap** bölümüne yaz. Hata bildirirken hata
mesajının tamamını ve hangi derste olduğunu ekle.
