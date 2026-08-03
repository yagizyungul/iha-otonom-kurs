---
theme: default
title: Bölüm 0 — Kursa Giriş
titleTemplate: '%s'
aspectRatio: 16/9
canvasWidth: 980
lineNumbers: false
# Tema açık sabitlensin: sistem koyu temaya geçse bile slaytlar değişmemeli,
# yoksa haftalar boyunca çekimler arasında renk kayması olur.
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
     BÖLÜM 0 — KURSA GİRİŞ · 3 ders · 13 slayt · ~13 dakika

     0.1 Bu kursta ne yapacağız?      slayt 1-5    5 dk
     0.2 Kime uygun, ön koşullar      slayt 6-9    4 dk
     0.3 Kurs kaynakları              slayt 10-13  4 dk

     KURAL (bolum-03'ten devralındı): slayt kesin terimi yazar,
     benzetmeyi eğitmen SÖZLÜ yapar. Slaytta analoji yok.

     GÖRSELLER: kesikli çerçeveli kutular henüz gelmemiş görsellerin
     yeri. Dosya adı kutunun içinde yazıyor; görsel geldiğinde
     public/gorseller/ altına o adla koy, kutuyu <figure> ile değiştir.
     Tam liste: public/gorseller/GEREKLI_GORSELLER.md
     ═══════════════════════════════════════════════════════════ -->

<!-- ─────────── 1 · KAPAK ─────────── -->

<div class="ky-kapak-serit"></div>

# ArduPilot + Gazebo ile<br>Otonom İHA Simülasyonu

<div class="ky-kapak-alt">

Bölüm 0 · Kursa Giriş

</div>

---

<!-- ─────────── 2 · 0.1 · KURS SONUNDA ─────────── -->

# Kurs sonunda yapabileceklerin

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>3 uçaklı</strong> Gazebo + ArduPilot simülasyonunu
      sıfırdan kurmak
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Python</strong> ile uçağı otonom kalkış, görev ve
      iniş yaptırmak
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Kamera akışını</strong> işleyip hedef tespiti
      yapmak
    </div>
  </div>

</div>

---

<!-- ─────────── 3 · FİNAL DEMO (tam ekran) ───────────
     Udemy önizleme dersinin karesi bu. En etkileyici görüntü buraya. -->

<div class="ky-tam-gorsel">
  <img src="/gorseller/b0-final-demo.jpg" alt="Gazebo'da pistte hazır bekleyen üç uçak">
</div>
<div class="ky-tam-yazi">

# Bitirdiğinde ekranın böyle görünecek

Üç uçak, tek dünya — hepsini kendi kodunla uçuracaksın.

</div>

---

<!-- ─────────── 4 · YOL HARİTASI ─────────── -->

# Yol haritası

<div class="ky-ikili">

<div>

<!-- Maddeler bilerek kısa: sarma yapan her satır slaydı alt şeride
     doğru 45px büyütüyor, dokuz maddede kutuya yer kalmıyor. -->

- **1 ·** Temel kavramlar ve mimari
- **2 ·** Ortam kurulumu
- **3 ·** İlk uçuş: tekten üç uçağa
- **4 ·** Uçuş modları ve görevler
- **5 ·** MAVLink protokolü

</div>

<div>

- **6 ·** pymavlink ile programlama
- **7 ·** Kamera ve görüntü işleme
- **8 ·** Çoklu bilgisayar senaryosu
- **9 ·** Sorun giderme ve kapanış

</div>

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Sıra önemli</div>
  Her bölüm bir öncekinin üstüne kuruluyor — atlamadan ilerle.
</div>

---

<!-- ─────────── 5 · NEDEN SİMÜLASYON ─────────── -->

# Neden simülasyon?

<div class="ky-ikili">

<div>

- Gerçek uçak, kart ve saha **gerektirmez**
- Hatalı komut hiçbir şeye **zarar vermez**
- Aynı senaryo **defalarca** tekrarlanır
- Otopilot yazılımı gerçek uçaktakiyle **aynı**

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/sitl_images.jpeg" alt="Çalışan SITL simülasyonu">
  </div>
  <figcaption>Çalışan SITL: solda telemetri, sağda haritadaki konum</figcaption>
</figure>

</div>

---

<!-- ─────────── 6 · 0.2 · KİME UYGUN ─────────── -->

# Bu kurs kimin için?

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">🛩</div>
    <div class="ky-kart__govde">
      <strong>Yarışma takımları</strong><br>
      TEKNOFEST ve benzeri İHA yarışmalarına hazırlananlar
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">🎓</div>
    <div class="ky-kart__govde">
      <strong>Mühendislik öğrencileri</strong><br>
      Bitirme projesi, ders projesi veya kariyer hazırlığı
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">⚙</div>
    <div class="ky-kart__govde">
      <strong>Hobi pilotları</strong><br>
      Otonom uçuşa geçmek isteyen model uçak kullanıcıları
    </div>
  </div>

</div>

---

<!-- ─────────── 7 · ÖN KOŞULLAR ─────────── -->

# Ön koşullar

<div class="ky-ikili">

<div>

**Bilgisayar**

- 8 GB RAM (16 GB rahat eder)
- 40 GB boş disk
- Ayrık ekran kartı önerilir

**Bilgi**

- Python'da değişken ve döngü
- Terminal deneyimi **gerekmiyor** — Bölüm 2'de öğretiliyor

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b0-ubuntu-masaustu.jpg" alt="Ubuntu 22.04 masaüstü">
  </div>
  <figcaption>Ubuntu 22.04 — kursun tamamı bu sistem üzerinde</figcaption>
</figure>

</div>

---

<!-- ─────────── 8 · NEYE İHTİYACIN YOK ───────────
     Sıfırdan başlayanın en büyük çekincesi "donanım almam gerekir mi".
     Bu slayt satın alma engelini kaldırıyor, o yüzden var. -->

# Neye ihtiyacın **yok**

<div class="ky-ikili">

<div>

- **Uçuş kartı yok** — Pixhawk almana gerek yok
- **Uçak yok** — model uçak gerekmiyor
- **Saha yok** — masanın başından çıkmıyorsun
- **ROS 2 yok** — bu kurs ROS bilmeden çalışır

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/pixhawk.jpg" alt="Uçuş kartı">
  </div>
  <figcaption>Gerçek bir uçuş kartı — bu kursta ihtiyacımız yok</figcaption>
</figure>

</div>

---

<!-- ─────────── 9 · NASIL ÇALIŞMALI ─────────── -->

# Nasıl çalışmalısın

<div class="ky-ikili">

<div>

- Videoyu **durdur**, komutu kendin yaz
- Kodu kopyalama — **elle yaz**, hata yap
- Bölüm sonu ödevini **atlama**
- Takıldığında Bölüm 9'a bak

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Hata alacaksın</div>
  Bu normaldir ve kursun bir parçasıdır. En sık görülen hataların
  hepsi <strong>Bölüm 9</strong>'da tek tek çözülüyor.
</div>

</div>

---

<!-- ─────────── 10 · 0.3 · KURS DEPOSU ─────────── -->

# Kurs deposu

<div class="ky-ikili">

<div>

```
iha-otonom-kurs/
├── kurulum/     kurulum script'leri
├── kod/         bölüm bölüm Python
├── gorevler/    .waypoints dosyaları
└── ODEVLER.md
```

Her dersin kodu **çalışır halde** depoda.

</div>

<div class="ky-gorsel-yer">
  GÖRSEL<br>
  <code>b0-github-depo.png</code><br>
  GitHub deposunun ana sayfası · en az 960×720
</div>

</div>

---

<!-- ─────────── 11 · REHBER ─────────── -->

# Yanındaki yazılı rehber

<div class="ky-ikili ky-ikili--ters">

<div>

- Bütün komutlar **kopyalanabilir** halde
- Kurulum adımları **numaralı**
- Sorun giderme bölümü ayrı

Videoyu izlerken rehberi açık tut; komutu videodan
oku, rehberden kopyala.

</div>

<div class="ky-gorsel-yer">
  GÖRSEL<br>
  <code>b0-rehber-pdf.png</code><br>
  PDF rehberin kapağı veya bir kurulum sayfası · en az 960×720
</div>

</div>

---

<!-- ─────────── 12 · DESTEK ─────────── -->

# Takıldığında

<!-- Üç madde önce alt alta kutuydu; üçüncüsü marka şeridinin altına
     iniyordu. Kart ızgarası yatay olduğu için yükseklik sorunu bitiyor. -->

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>Önce Bölüm 9</strong><br>
      Hataların büyük kısmı sorun giderme bölümünde çözülü
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Sürüm notları</strong><br>
      Depodaki <code>SURUM_NOTLARI.md</code> güncel farkları listeler
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Soru-Cevap</strong><br>
      Hata mesajının tamamını ve ders numarasını yaz
    </div>
  </div>

</div>

---

<!-- ─────────── 13 · SONRAKİ BÖLÜM ─────────── -->

# Özet

- Kurs sonunda **3 uçaklı** simülasyonu kurup Python ile uçuracaksın
- Donanım, saha ve ROS 2 bilgisi **gerekmiyor**
- Depoda her dersin **çalışan** kodu var

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Sonraki bölüm</div>
  <strong>Bölüm 1 — Temel kavramlar:</strong> uçuş kontrolcüsü nedir,
  SITL ne işe yarar ve sistemin üç katmanı nasıl konuşur.
</div>
