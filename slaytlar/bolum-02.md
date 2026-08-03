---
theme: default
title: Bölüm 2 — Ortam Kurulumu
titleTemplate: '%s'
aspectRatio: 16/9
canvasWidth: 980
lineNumbers: false
colorSchema: light
fonts:
  sans: 'Figtree'
  mono: 'JetBrains Mono'
  weights: '400,500,600,700'
  italic: false
transition: none
mdc: true
---

<!-- ═══════════════════════════════════════════════════════════
     BÖLÜM 2 — ORTAM KURULUMU · 11 ders · 16 slayt · ~90 dakika

     Bu bölüm TERMİNAL ağırlıklı. Slaytlar sadece noktalama işareti:
     her dersin başında "ne yapacağız", tuzaklarda uyarı, sonda özet.
     Komutların tamamı çekim metninde (yeşil kutular).

     Ders → slayt eşlemesi:
       2.1  Ubuntu kurulumu          slayt 4-5
       2.2  Terminal temel           slayt 6
       2.3  Sistem paketleri         slayt 7
       2.4  ArduPilot derleme        slayt 8
       2.5  NumPy tuzağı             slayt 9
       2.6  İlk SITL testi           (slayt yok — terminal)
       2.7  Gazebo Harmonic          slayt 10
       2.8  Kütüphaneler/GStreamer   slayt 11
       2.9  Plugin derleme           slayt 12
       2.10 Modeller                 slayt 13
       2.11 Ortam değişkenleri       slayt 14-15

     KAYNAKTAN DOĞRULANDI (Ubuntu 22.04.5 · 3 Ağustos 2026):
       - MAVProxy 1.8.74 + numpy 2.2.6 SORUNSUZ. Rehberdeki
         "numpy<2 KRİTİK" adımı artık geçersiz.
       - Taze 22.04'te pip 22.0.2 var, --break-system-packages
         bayrağı YOK. O bayrak 24.04 (PEP 668) için.
       - Plugin yolu: /usr/local/lib/ardupilot_gazebo/
       - Gazebo Sim 8.12.0 (Harmonic), jammy deposundan
     ═══════════════════════════════════════════════════════════ -->

<!-- ─────────── 1 · KAPAK ─────────── -->

<div class="ky-kapak-serit"></div>

# Ortam Kurulumu

<div class="ky-kapak-alt">

Bölüm 2 · Sıfırdan çalışan simülasyona

</div>

---

<!-- ─────────── 2 · BU BÖLÜMDE ─────────── -->

# Bu bölümde

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>ArduPilot</strong> — beyni kaynaktan derleyeceğiz
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Gazebo Harmonic</strong> — sanal dünyayı kuracağız
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Köprü</strong> — ikisini birbirine bağlayacağız
    </div>
  </div>

</div>

---

<!-- ─────────── 3 · KURULUM SIRASI ─────────── -->

# Kurulum sırası

- **1 ·** Sistem hazırlığı — derleme araçları
- **2 ·** ArduPilot — beyin
- **3 ·** Gazebo Harmonic — dünya
- **4 ·** Köprü, modeller ve yollar

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Sıra değiştirilemez</div>
  Köprü, ikisi kurulmadan <strong>derlenmez</strong>.
</div>

---

<!-- ─────────── 4 · 2.1 · İŞLETİM SİSTEMİ ─────────── -->

# Hangi işletim sistemi?

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">✓</div>
    <div class="ky-kart__govde">
      <strong>Ubuntu 22.04</strong><br>
      Dual boot — en iyi performans, kursun referans sistemi
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">~</div>
    <div class="ky-kart__govde">
      <strong>Sanal makine</strong><br>
      Kolay ve geri dönülebilir, 3B grafik yavaş
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">◷</div>
    <div class="ky-kart__govde">
      <strong>WSL2 / macOS</strong><br>
      Çalışır ama Gazebo için ek uğraş ister
    </div>
  </div>

</div>

---

<!-- ─────────── 5 · UYARI: YEDEK ─────────── -->

# Dual boot öncesi

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Disk bölümleme veri kaybettirebilir</div>
  Kuruluma başlamadan önce <strong>bütün verilerini yedekle</strong>.
  Bu adımı atlayıp sonra pişman olan çok.
</div>

- Ubuntu **22.04 LTS** ISO indir, USB'ye yaz
- Windows'ta **80 GB** boş alan aç
- Kurulumda "Install alongside" seç

---

<!-- ─────────── 6 · 2.2 · TERMİNAL ─────────── -->

# Terminalde hayatta kalma

```
ls        listele        cd     klasöre gir
pwd       neredeyim      mkdir  klasör oluştur
cp / mv   kopyala/taşı   rm     sil (dikkat!)
cat       dosyayı göster nano   düzenle
sudo      yönetici       apt    program kur
```

Tab **tamamlar**, Yukarı ok **önceki komutu** getirir,
Ctrl+C **durdurur**.

---

<!-- ─────────── 7 · 2.3 · NE KURUYORUZ ─────────── -->

# Sistem paketleri

<div class="ky-ikili">

<div>

- **git** — kaynak kodu indirme
- **build-essential, cmake** — C++ derleme
- **python3-dev, pip** — Python eklentileri
- **gdal** — harita/coğrafi veri

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Neden derleme aracı?</div>
  ArduPilot ve köprü eklentisi hazır paket olarak gelmiyor;
  ikisini de <strong>kaynaktan</strong> derleyeceğiz.
</div>

</div>

---

<!-- ─────────── 8 · 2.4 · ARDUPILOT ─────────── -->

# ArduPilot: dört adım

```
git clone .../ardupilot.git      # kaynağı indir
git submodule update --init      # alt modüller
install-prereqs-ubuntu.sh -y     # bağımlılıklar
./waf configure --board sitl     # yapılandır
./waf plane                      # derle
```

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Derleme uzun sürer</div>
  İlk derleme makineye göre <strong>5–20 dakika</strong>. Bir kez.
</div>

---

<!-- ─────────── 9 · 2.5 · TUZAK 1 ─────────── -->

# Tuzak 1 — harita penceresi açılmıyor

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">AttributeError: _ARRAY_API not found</div>
  MAVProxy'nin konsol ve harita pencereleri açılmaz.
</div>

- **Sebep:** derlenmiş modüller NumPy'ın **farklı sürümüne** göre kurulmuş
- **Çözüm:** MAVProxy'yi güncelle — `pip3 install -U MAVProxy`
- Güncel MAVProxy ile NumPy 2 **sorun çıkarmıyor**

---

<!-- ─────────── 10 · 2.7 · GAZEBO ─────────── -->

# Gazebo Harmonic

<div class="ky-ikili">

<div>

- OSRF deposunu **ekle**
- `gz-harmonic` paketini **kur**
- `gz sim shapes.sdf` ile **test et**

Ubuntu 22.04 için depo adı: `jammy`

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Doğru sürüm önemli</div>
  Gazebo'nun eski (Classic) ve yeni sürümleri ayrı programlar.
  Bize <strong>Harmonic</strong> lazım — komut adı <code>gz</code>.
</div>

</div>

---

<!-- ─────────── 11 · 2.8 · KÜTÜPHANELER ─────────── -->

# Köprü için kütüphaneler

<div class="ky-ikili">

<div>

- **libgz-\*-dev** — Gazebo başlık dosyaları
- **rapidjson** — JSON okuma
- **libopencv** — görüntü işleme
- **gstreamer** — video akışı

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Şimdi kuruyoruz, Bölüm 7'de kullanacağız</div>
  GStreamer kamera yayını için gerekli. Eklentiyle birlikte
  derlendiği için sonradan eklemek zor.
</div>

</div>

---

<!-- ─────────── 12 · 2.9 · TUZAK 2 ─────────── -->

# Tuzak 2 — plugin bulunamıyor

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">ArduPilotPlugin not found</div>
  Yola dosyanın <strong>kendisi</strong> yazıldığında çıkar.
</div>

```
✗ .../ardupilot_gazebo/libArduPilotPlugin.so
✓ .../ardupilot_gazebo
```

Yola **dizin** yazılır, dosya değil. Ayrıca komut **tek satırda** olmalı.

---

<!-- ─────────── 13 · 2.10 · MODELLER ─────────── -->

# Uçak modelleri

<div class="ky-ikili">

<div>

- **SITL_Models** — ArduPilot'un resmi model deposu
- **UAV paketi** — kursun üç uçağı ve dünyası
- Modeller `.sdf` dosyalarıdır — XML

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Python paketleri</div>
  <code>pymavlink</code>, <code>opencv-python</code> ve arkadaşları
  da burada kuruluyor. Ubuntu 24.04'teysen
  <code>--break-system-packages</code> ekle.
</div>

</div>

---

<!-- ─────────── 14 · 2.11 · ORTAM DEĞİŞKENLERİ ─────────── -->

# Ortam değişkenleri

Gazebo, eklentiyi ve modelleri **nerede arayacağını** bilmiyor:

```
GZ_VERSION               harmonic
GZ_SIM_SYSTEM_PLUGIN_PATH  köprü nerede
GZ_SIM_RESOURCE_PATH       modeller nerede
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Kalıcı yapmazsan</div>
  Terminal kapanınca kaybolur — <code>~/.bashrc</code>'ye yazıyoruz.
</div>

---

<!-- ─────────── 15 · DOĞRULAMA ─────────── -->

# Kurulum doğrulama

```
which sim_vehicle.py     # ArduPilot yolda mı
gz sim --version         # Gazebo sürümü
echo $GZ_SIM_RESOURCE_PATH
ls /usr/local/lib/ardupilot_gazebo
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Dördü de cevap veriyorsa</div>
  Kurulum tamam. Bir sonraki bölümde uçuyoruz.
</div>

---

<!-- ─────────── 16 · ÖZET ─────────── -->

# Özet

- ArduPilot ve köprü **kaynaktan** derlendi
- Gazebo Harmonic depodan kuruldu
- Modeller yerleşti, yollar `~/.bashrc`'ye yazıldı
- İki tuzak: **NumPy uyumu** ve **plugin yolu**

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Sonraki bölüm</div>
  <strong>Bölüm 3 — İlk uçuş:</strong> tek uçaktan üç uçağa.
</div>
