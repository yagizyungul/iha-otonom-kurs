---
theme: default
title: Bölüm 2 — Yazılım Kurulumu
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
     BÖLÜM 2 — YAZILIM KURULUMU (2B) · 10 ders · ~96 dakika

       2.9   Terminal hayatta kalma kiti   slayt 3-5     13 dk
       2.10  Sistem paketleri              slayt 6-8      6 dk
       2.11  ArduPilot kaynaktan           slayt 9-12    10 dk
       2.12  NumPy tuzağı                  slayt 13-14    6 dk
       2.13  İlk test: sim_vehicle.py      slayt 15-16    5 dk
       2.14  Gazebo Harmonic               slayt 17-19    7 dk
       2.15  Köprü kütüphaneleri           slayt 20-21    6 dk
       2.16  Plugin derleme + yol tuzağı   slayt 22-25   10 dk
       2.17  SITL_Models ve UAV modelleri  slayt 26-28    8 dk
       2.18  PATH, Python paketleri, test  slayt 29-33   10 dk

     ── 2A NEREDE ──
     İşletim sistemi kurulumu (2.1-2.8) bu dosyadan ÇIKARILDI; çekimi
     7 Ağustos 2026'da tamamlandı. 46 slaytlık hâli burada duruyor:
       ~/Desktop/Udemy/arsiv/bolum-02A-isletim-sistemi/

     ── KOMUTLARIN KAYNAĞI ──
     Simülasyon-Ders-Rehberi.docx.pdf · Adım 3, 5, 6, 7, 8, 9, 10, 11, 12

     ── 7 AĞUSTOS 2026'DA DOĞRULANDI ──
     Ubuntu 22.04.5 · x86_64 · Python 3.10.12
     Adım 3 ve 7'deki 20 apt paketinin tamamı depoda mevcut.
     OSRF deposu, üç GitHub deposu erişilebilir (HTTP 200).
     libgz-sim8-dev 8.14.0-1~jammy · libgz-cmake3-dev 3.6.0-1~jammy
     Komutlar ÇALIŞTIRILARAK test EDİLMEDİ — bilerek: makine çekim için
     temizlenmiş durumda, çalıştırmak o durumu harcardı.
     ═══════════════════════════════════════════════════════════ -->

<!-- ─────────── 1 · KAPAK ─────────── -->

<div class="ky-kapak-serit"></div>

# Yazılım Kurulumu

<div class="ky-kapak-alt">

Bölüm 2B · Boş Ubuntu'dan çalışan simülasyona

</div>

---

<!-- ─────────── 2 · KURULUM SIRASI ─────────── -->

# Kurulum sırası

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>Sistem</strong><br>derleme araçları, Python
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>ArduPilot</strong><br>uçağın beyni
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Gazebo</strong><br>uçtuğu dünya
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">4</div>
    <div class="ky-kart__govde">
      <strong>Köprü</strong><br>ikisini bağlayan eklenti
    </div>
  </div>

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Sıra değiştirilemez</div>
  Köprü eklentisi, ArduPilot ve Gazebo <strong>kurulmadan derlenmez</strong>.
</div>

---

<!-- ─────────── + · SONUNDA NE OLACAK ─────────── -->

# Sonunda ne olacak?

<div class="ky-ikili">

<div>

Bu bölümün sonunda bilgisayarında **üç uçağın aynı anda uçtuğu** bir
simülasyon çalışıyor olacak.

Şimdi boş bir Ubuntu var. İki saat sonra burası bir **uçuş
laboratuvarı**.

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b2-gazebo-uc-ucak.png" alt="Gazebo'da üç uçak">
  </div>
  <figcaption>Bölüm 3'ün sonu — üç UAV, tek dünya</figcaption>
</figure>

</div>

---

<!-- ═══════ 2.9 · TERMİNAL ═══════ -->
<!-- ─────────── 3 · TERMİNAL NEDİR ─────────── -->

# Terminal

<div class="ky-ikili">

<div>

Bilgisayara **yazıyla** talimat verdiğin pencere. Bu bölümdeki her
işlem buradan yapılacak.

Açmak için: **Ctrl + Alt + T**

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Komut istemi</div>
  <code>yagiz@makine:~$</code><br><br>
  <code>~</code> ev dizinin, <code>$</code> "komutunu bekliyorum" demek.
</div>

</div>

---

<!-- ─────────── 4 · TEMEL KOMUTLAR ─────────── -->

# Komutlar · nerede olduğun

```bash
ls            bulunduğun klasörü listele
cd ~/klasor   klasöre gir      (cd ..  bir üste)
pwd           neredeyim
mkdir -p yol  klasör oluştur
```

Bu dördü ile dosya sisteminde **gezinirsin**.

---

<!-- ─────────── + · KOMUTLAR 2 ─────────── -->

# Komutlar · iş yapanlar

```bash
cp / mv       kopyala / taşı
rm -rf yol    sil — geri dönüşü YOK
cat dosya     içeriğini göster
nano dosya    metin düzenleyicide aç
sudo komut    yönetici yetkisiyle çalıştır
apt           program kur / kaldır
```

---

<!-- ─────────── 5 · KISAYOLLAR ─────────── -->

# Hayat kurtaran kısayollar

<div class="ky-ikili">

<div>

- **Tab** → komutu/dosya adını tamamlar
- **↑ ↓** → önceki komutları getirir
- **Ctrl + C** → çalışan komutu durdurur
- **Ctrl + L** ya da `clear` → ekranı temizler

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Tab'ı alışkanlık yap</div>
  Uzun dizin adlarını elle yazma. Birkaç harf yazıp Tab'a bas —
  yazım hatası riskini sıfıra indirir.
</div>

</div>

---

<!-- ─────────── + · YOUTUBE ─────────── -->

# Daha fazla pratik istersen

<div class="ky-ikili">

<div>

Bu konularla ilgili **ücretsiz videolar** YouTube'da:

### Yağız Yungul

Terminal, Linux temelleri ve İHA simülasyonu üzerine ayrı ayrı
anlatımlar var.

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Zorunlu değil</div>
  Buradan devam etmende hiçbir sakınca yok — kurs kendi başına
  bütün. Ama pratiğini geliştirmek istersen orada da bakabilirsin.
</div>

</div>

---

<!-- ═══════ 2.10 · SİSTEM PAKETLERİ ═══════ -->
<!-- ─────────── 6 · GÜNCELLEME ─────────── -->

# Önce sistemi güncelle

<!-- KOMUT -->
```bash
sudo apt update && sudo apt upgrade -y
```

- `apt update` → depo **listesini** tazeler, program kurmaz
- `apt upgrade` → kurulu programları **yeni sürüme** çıkarır
- `-y` → her soruya "evet" der

<div class="ky-kutu">
  <div class="ky-kutu__baslik">İlk çalıştırmada uzun sürebilir</div>
  Taze bir Ubuntu'da yüzlerce paket güncellenir. Kahve molası.
</div>

---

<!-- ─────────── + · APT NEDİR ─────────── -->

# `apt` nedir?

<div class="ky-ikili">

<div>

Ubuntu'nun **uygulama mağazası**. Telefonundaki Play Store ne yapıyorsa
`apt` de onu yapar — ama komut satırından.

- Program **arar**
- **Kurar**, bağımlılıklarıyla birlikte
- **Günceller** ve **kaldırır**

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik"><code>sudo</code> neden şifre soruyor?</div>
  Program kurmak sistemin ortak alanına yazmak demek. Ubuntu bunu
  gelişigüzel yaptırmıyor; <strong>yönetici yetkisi</strong> istiyor.
</div>

</div>

---
class: kod-sm
---

<!-- ─────────── 7 · TEMEL PAKETLER ─────────── -->

# Derleme araçları

<!-- KOMUT -->
```bash
sudo apt install -y \
  git python3-pip python3-venv python3-dev \
  wget curl gnupg lsb-release \
  software-properties-common \
  build-essential cmake pkg-config
```

Satır sonundaki `\` komutun **devam ettiğini** söyler.

---

<!-- ─────────── 8 · NE KURDUK ─────────── -->

# Ne kurduk?

<div class="ky-ikili">

<div>

- **git** → kaynak kodu indirmek
- **build-essential** → C/C++ derleyicisi
- **cmake** → derleme yapılandırıcısı
- **python3-dev** → Python eklentileri derlemek
- **gdal** → harita/coğrafi veri

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Neden derleyici?</div>
  ArduPilot ve köprü eklentisi hazır paket olarak gelmiyor.
  İkisini de <strong>kaynaktan</strong> derleyeceğiz.
</div>

</div>

<!-- KOMUT -->
```bash
sudo apt install -y gdal-bin libgdal-dev \
  python3-gdal imagemagick
```

---

<!-- ─────────── + · DERLEME NEDİR ─────────── -->

# Derleme nedir?

Yazılım iki biçimde dağıtılır:

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">◉</div>
    <div class="ky-kart__govde">
      <strong>Hazır paket</strong><br>
      Çalıştırılabilir hâlde gelir. <code>apt install</code> yeter.
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">⚙</div>
    <div class="ky-kart__govde">
      <strong>Kaynak kod</strong><br>
      İnsan yazısı. Makinenin anlayacağı hâle <strong>çevrilmesi</strong>
      gerekir — buna derleme denir.
    </div>
  </div>

</div>

ArduPilot ve köprü eklentisi ikinci gruptan. Bu yüzden `build-essential`
ve `cmake` kurduk.

---

<!-- ═══════ 2.11 · ARDUPILOT ═══════ -->
<!-- ─────────── 9 · KAYNAĞI İNDİR ─────────── -->

# ArduPilot'u indir

<!-- KOMUT -->
```bash
cd ~
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
git submodule update --init --recursive
```

`submodule`, ArduPilot'un kullandığı **alt depoları** çekiyor.

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Submodule adımını atlama</div>
  Atlarsan derleme yarıda <strong>hata verir</strong> — en sık yapılan hata bu.
</div>

---

<!-- ─────────── + · GITHUB ─────────── -->

# Kaynak nereden geliyor?

ArduPilot **GitHub**'da açık kaynak; `git clone` deponun tam kopyasını
geçmişiyle birlikte indiriyor.

<figure class="ky-gorsel ky-gorsel--genis">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b2-github-ardupilot.png" alt="ArduPilot GitHub deposu">
  </div>
  <figcaption>github.com/ArduPilot/ardupilot — 15,6 bin yıldız, 73 bin commit</figcaption>
</figure>

---

<!-- ─────────── 10 · BAĞIMLILIKLAR ─────────── -->

# Bağımlılıkları kur

<!-- KOMUT -->
```bash
Tools/environment_install/install-prereqs-ubuntu.sh -y
source ~/.profile
```

ArduPilot'un kendi hazırladığı script; gerekli her paketi kurar.

<div class="ky-kutu">
  <div class="ky-kutu__baslik"><code>source ~/.profile</code> neden var?</div>
  Script <code>PATH</code>'e yeni dizinler ekliyor. <code>source</code>
  bu değişikliği <strong>açık terminale</strong> uygular; yoksa yeni bir
  terminal açman gerekirdi.
</div>

---

<!-- ─────────── 11 · DERLE ─────────── -->

# Derle

<!-- KOMUT -->
```bash
./waf configure --board sitl
./waf plane
```

- `--board sitl` → gerçek kart değil, **simülasyon**
- `waf plane` → sabit kanat firmware'i

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Derleme 5–20 dakika</div>
  Videoyu burada kesiyorum, bitince kaldığımız yerden devam edeceğiz.
</div>

---

<!-- ─────────── 12 · DOĞRULA ─────────── -->

# Derleme başarılı mı?

<!-- KOMUT -->
```bash
ls -la ~/ardupilot/build/sitl/bin/arduplane
```

Dosya varsa derleme tamam.

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Hata aldıysan</div>
  Neredeyse her zaman iki sebepten: <strong>submodule</strong> adımı
  atlanmış ya da <code>install-prereqs</code> yarıda kesilmiş.
  İkisini tekrar çalıştır.
</div>

---

<!-- ─────────── + · KONTROL NOKTASI 1 ─────────── -->

# Buraya kadar ne yaptık?

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">✓</div>
    <div class="ky-kart__govde">
      <strong>Sistem</strong><br>derleme araçları kuruldu
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">✓</div>
    <div class="ky-kart__govde">
      <strong>ArduPilot</strong><br>indirildi ve derlendi
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">→</div>
    <div class="ky-kart__govde">
      <strong>Sırada</strong><br>uçağın beynini ilk kez çalıştırmak
    </div>
  </div>

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Ara verecek yer burası</div>
  Uzun derleme bitti. Devamı daha hızlı ilerleyecek.
</div>

---

<!-- ═══════ 2.12 · NUMPY TUZAĞI ═══════ -->
<!-- ─────────── 13 · TUZAK ─────────── -->

# Tuzak — harita penceresi açılmıyor

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">AttributeError: _ARRAY_API not found</div>
  SITL çalışır ama MAVProxy'nin <strong>konsol ve harita</strong>
  pencereleri açılmaz.
</div>

- **Sebep:** MAVProxy'nin derlenmiş modülleri NumPy'ın **eski**
  sürümüne göre kurulmuş, sistemde **NumPy 2** var
- İki çözüm var, ikisi de çalışıyor

---

<!-- ─────────── 14 · İKİ ÇÖZÜM ─────────── -->

# İki çözüm

```bash
# A · NumPy'ı 1.x'e sabitle — rehberin yolu
pip3 install --break-system-packages "numpy<2"
```

<!-- KOMUT -->
```bash
# B · MAVProxy'yi güncelle — bu kursta bunu kullanıyoruz
pip3 install --break-system-packages -U MAVProxy
```

<!-- KOMUT -->
```bash
sudo apt install -y python3-tk python3-wxgtk4.0
```

Üçüncü satır, MAVProxy'nin pencere çizmek için kullandığı
arayüz kütüphanelerini kuruyor.

---

<!-- ─────────── + · HANGİSİNİ SEÇMELİ ─────────── -->

# Hangisini seçmeli?

<div class="ky-kartlar ky-kartlar--kisa">

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">A</div>
    <div class="ky-kart__govde">
      NumPy'ı <strong>geriye çeker</strong>. Bu bölümde çalışır, ama
      Bölüm 7'de kuracağımız OpenCV ve YOLO NumPy 2 istiyor.
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">B</div>
    <div class="ky-kart__govde">
      MAVProxy'yi <strong>ileri alır</strong>. Güncel sürüm NumPy 2 ile
      sorunsuz çalışıyor — ikisi de memnun.
    </div>
  </div>

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Bu kursta B</div>
  Rehberde A yazıyor; o rehber yazıldığında güncel MAVProxy henüz
  çıkmamıştı. Bugün B daha doğru.
</div>

---

<!-- ═══════ 2.13 · İLK TEST ═══════ -->
<!-- ─────────── 15 · İLK ÇALIŞTIRMA ─────────── -->

# İlk test

<!-- KOMUT -->
```bash
cd ~/ardupilot
sim_vehicle.py -v ArduPlane --console --map
```

Üç pencere açılmalı:

- **Terminal** → MAVProxy komut satırı
- **Konsol** → irtifa, hız, batarya, uçuş modu
- **Harita** → uçağın konumu

Kapatmak için terminalde **Ctrl + C**.

---

<!-- ─────────── 16 · İLK ÇALIŞTIRMA UZUN SÜRER ─────────── -->

# İlk çalıştırma yavaş

<div class="ky-ikili">

<div>

İlk `sim_vehicle.py` çağrısı eksik Python paketlerini indirir ve
parametre dosyalarını üretir.

Sonraki açılışlar **saniyeler** sürer.

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Buraya kadar geldiysen</div>
  Uçağın beyni çalışıyor. Gazebo olmadan, ArduPilot kendi basit
  fiziğiyle uçuyor. Sırada onu <strong>görünür</strong> yapmak var.
</div>

</div>

---

<!-- ─────────── + · MAVPROXY EKRANI ─────────── -->

# Ekranda ne görüyorsun?

<div class="ky-ikili">

<div>

**MAVProxy** açıldı — uçakla konuşan yer istasyonu programı.

- Uçak **havada değil**, yerde bekliyor
- Konsolda irtifa `0`, mod `MANUAL`
- Henüz komut vermedik

Uçurmayı Bölüm 3'te öğreneceğiz.

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b2-sitl-konsol.jpeg" alt="MAVProxy konsolu">
  </div>
  <figcaption>MAVProxy konsolu ve harita penceresi</figcaption>
</figure>

</div>

---
class: kod-sm
---

<!-- ═══════ 2.14 · GAZEBO ═══════ -->
<!-- ─────────── 17 · DEPO EKLEME ─────────── -->


# Gazebo deposunu ekle

<!-- KOMUT -->
```bash
sudo wget https://packages.osrfoundation.org/gazebo.gpg \
  -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
```

<!-- KOMUT -->
```bash
echo "deb [arch=$(dpkg --print-architecture) \
signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] \
http://packages.osrfoundation.org/gazebo/ubuntu-stable \
$(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/gazebo-stable.list
```

Gazebo Ubuntu'nun kendi deposunda yok; **OSRF'nin deposunu** ekliyoruz.

---

<!-- ─────────── 18 · KUR VE TEST ET ─────────── -->

# Gazebo Harmonic'i kur

<!-- KOMUT -->
```bash
sudo apt update
sudo apt install -y gz-harmonic
gz sim -v4 shapes.sdf
```

3D pencerede şekiller görüyorsan kurulum başarılı.

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Doğru Gazebo'yu kurduğuna emin ol</div>
  Gazebo'nun eski <strong>Classic</strong> ve yeni sürümleri ayrı
  programlar. Bize <strong>Harmonic</strong> lazım — komutu <code>gz</code>,
  eskisinin komutu <code>gazebo</code>.
</div>

---

<!-- ─────────── 19 · PENCERE AÇILMIYORSA ─────────── -->

# Ekran kartı neden önemli?

<div class="ky-ikili">

<div>

Gazebo iki ağır iş yapıyor: **3B çizim** ve **fizik hesabı**. İkisi de
ekran kartından güç alıyor.

Yanlış kart kullanılırsa ya pencere **hiç açılmaz**, ya da açılır ama
**5 FPS** gider — uçak zıplaya zıplaya uçar.

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Dizüstülerde iki kart var</div>
  Biri <strong>Intel</strong> (tasarruflu), biri <strong>NVIDIA</strong>
  (güçlü). Linux çoğu zaman varsayılan olarak Intel'i seçiyor.
</div>

</div>

---

<!-- ─────────── + · HANGİ KART ÇİZİYOR ─────────── -->

# Hangi kart çiziyor?

Önce ölçüm aracını kuruyoruz:

<!-- KOMUT -->
```bash
sudo apt install -y mesa-utils
```

<!-- KOMUT -->
```bash
glxinfo | grep "OpenGL renderer"
```

Bu komut tahmin etmeyi bitiriyor — o an **hangi kartın çizdiğini**
doğrudan söylüyor.

---

<!-- ─────────── + · ÇIKTIYI OKU ─────────── -->

# Çıktıyı oku

<div class="ky-kartlar ky-kartlar--kisa">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">✓</div>
    <div class="ky-kart__govde">
      <strong>NVIDIA GeForce…</strong><br>
      İdeal. Gazebo tam hızda çalışır.
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">~</div>
    <div class="ky-kart__govde">
      <strong>Mesa Intel…</strong><br>
      Çalışır ama yavaş. NVIDIA'n varsa ona geç.
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">✗</div>
    <div class="ky-kart__govde">
      <strong>llvmpipe</strong><br>
      Ekran kartı hiç kullanılmıyor — işlemci çiziyor.
    </div>
  </div>

</div>

`llvmpipe` görüyorsan sürücü kurulu değil demektir.

---

<!-- ─────────── + · SÜRÜCÜ ─────────── -->

# NVIDIA sürücüsü kurulu mu?

<!-- KOMUT -->
```bash
nvidia-smi
```

Tablo geliyorsa sürücü çalışıyor — üstte **sürüm**, altta **kart adı**
ve bellek yazar.

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">"command not found" diyorsa</div>
  Sürücü yok. <strong>Software &amp; Updates → Additional Drivers</strong>
  penceresinden tescilli NVIDIA sürücüsünü seç, kur, yeniden başlat.
</div>

---
class: kod-sm
---

<!-- ─────────── + · NVIDIA'YA ZORLA ─────────── -->

# Gazebo'yu NVIDIA'da çalıştır

Sürücü var ama `glxinfo` Intel diyorsa çizimi yönlendiriyoruz:

<!-- KOMUT -->
```bash
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia \
  glxinfo | grep "OpenGL renderer"
```

Şimdi NVIDIA yazıyorsa yöntem çalışıyor. Kalıcı kısayol:

<!-- KOMUT -->
```bash
echo "alias gznv='__NV_PRIME_RENDER_OFFLOAD=1 \
__GLX_VENDOR_LIBRARY_NAME=nvidia gz'" >> ~/.bashrc
```

Bundan sonra `gz sim` yerine **`gznv sim`** yazacaksın.

---

<!-- ─────────── + · WAYLAND / XORG ─────────── -->

# Wayland mı, Xorg mu?

<!-- KOMUT -->
```bash
echo $XDG_SESSION_TYPE
```

<div class="ky-ikili">

<div>

`x11` çıkmalı. `wayland` çıkıyorsa Gazebo ve NVIDIA yönlendirmesi sorun
çıkarabilir.

**Geçiş:** oturumu kapat → giriş ekranında **dişli** simgesi →
**Ubuntu on Xorg** → gir.

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Harici monitörde sadece imleç mi var?</div>
  Bu tam olarak Wayland sorunudur. Xorg'a geçince düzelir.
</div>

</div>

---

<!-- ─────────── + · HÂLÂ AÇILMIYORSA ─────────── -->

# Hâlâ açılmıyorsa

- **Sanal makinede:** VirtualBox → Ekran → **3B hızlandırma** açık,
  video belleği 128 MB
- **Uzak bağlantıda** (SSH/RDP): 3B çizim gitmez, makinenin başına geç
- **Açılıyor ama yavaş:** Gazebo'da gölgeleri kapat, pencereyi küçült

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Bu ders için ölçüt</div>
  <code>gz sim -v4 shapes.sdf</code> açılıyor ve akıcı dönüyorsa yeterli.
</div>

---

<!-- ─────────── + · GAZEBO NE YAPIYOR ─────────── -->

# Gazebo tam olarak ne yapıyor?

<div class="ky-ikili">

<div>

Uçağın uçtuğu **sanal dünyayı** hesaplıyor:

- **Fizik** — yerçekimi, rüzgâr, çarpışma
- **Sensörler** — kamera, GPS, IMU
- **Görselleştirme** — 3B pencere

ArduPilot "kanadı 5 derece kır" diyor; **Gazebo** uçağın buna nasıl
tepki vereceğini hesaplıyor.

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Bu ders için yeterli olan</div>
  <code>shapes.sdf</code> açılıyorsa kurulum tamam. Performans ayarını
  Bölüm 9'da ele alacağız.
</div>

</div>

---

<!-- ─────────── + · KONTROL NOKTASI 2 ─────────── -->

# İki program, henüz birbirinden habersiz

```mermaid {theme: 'base', scale: 0.95, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '20px', fontFamily: 'Figtree'}}
flowchart LR
  A[ArduPilot<br/>uçağın beyni] -.->|bağlantı YOK| B[Gazebo<br/>3B dünya]
  style A fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
  style B fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
```

İkisi de çalışıyor ama birbirini görmüyor. ArduPilot kendi basit
fiziğini kullanıyor, Gazebo boş bir dünya gösteriyor.

**Sırada bu boşluğu kapatmak var.**

---
class: kod-sm
---

<!-- ═══════ 2.15 · KÖPRÜ KÜTÜPHANELERİ ═══════ -->
<!-- ─────────── 20 · GELİŞTİRME PAKETLERİ ─────────── -->


# Köprü için geliştirme paketleri

<!-- KOMUT -->
```bash
sudo apt install -y \
  libgz-sim8-dev libgz-cmake3-dev libgz-transport13-dev \
  libgz-msgs10-dev libgz-common5-dev libgz-math7-dev \
  libgz-plugin2-dev libgz-rendering8-dev \
  libgz-sensors8-dev libgz-gui8-dev
sudo apt install -y rapidjson-dev libopencv-dev
```

Bu paketler ancak **depo eklendikten sonra** görünür — sıranın sebebi bu.

---
class: kod-sm
---

<!-- ─────────── 21 · GSTREAMER ─────────── -->

# GStreamer

<!-- KOMUT -->
```bash
sudo apt install -y \
  libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
  gstreamer1.0-plugins-bad gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-ugly gstreamer1.0-libav \
  gstreamer1.0-gl gstreamer1.0-tools gstreamer1.0-x
```

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Şimdi kuruyoruz, Bölüm 7'de kullanacağız</div>
  Kamera yayını için gerekli. Eklentiyle <strong>birlikte derlendiği</strong>
  için sonradan eklemek yeniden derleme demek.
</div>

---

<!-- ═══════ 2.16 · PLUGIN ═══════ -->
<!-- ─────────── 22 · KÖPRÜ NEDİR ─────────── -->

# Köprü ne işe yarıyor?

<div class="ky-ikili">

<div>

`ardupilot_gazebo`, iki programı birbirine bağlayan eklenti.

- Gazebo'daki **sensör verisi** → ArduPilot'a
- ArduPilot'un **motor komutları** → Gazebo'ya

Bu eklenti olmadan ikisi birbirinden habersiz çalışır.

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b2-kopru-semasi.png" alt="ArduPilot–Gazebo köprü şeması">
  </div>
  <figcaption>Sensör verisi ve motor komutları — iki yönlü akış</figcaption>
</figure>

</div>

---

<!-- ─────────── + · KÖPRÜ ŞEMASI ─────────── -->

# Köprü kurulunca

```mermaid {theme: 'base', scale: 0.9, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '19px', fontFamily: 'Figtree'}}
flowchart LR
  G[Gazebo] -->|IMU, GPS<br/>port 9002| A[ArduPilot]
  A -->|motor komutları| G
  A -->|MAVLink<br/>port 14550| M[MAVProxy]
  style G fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
  style A fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
  style M fill:#ffffff,stroke:#dde1e8,stroke-width:2px,color:#5a6473
```

Gazebo **sensör verisi** gönderiyor, ArduPilot **motor komutu** dönüyor.
Saniyede yüzlerce kez.

---

<!-- ─────────── 23 · DERLE ─────────── -->

# Eklentiyi derle

<!-- KOMUT -->
```bash
export GZ_VERSION=harmonic
cd ~
git clone https://github.com/ArduPilot/ardupilot_gazebo.git
cd ardupilot_gazebo
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j$(nproc)
sudo make install
```

`-j$(nproc)` → **tüm çekirdekleri** kullan, derleme hızlansın.

---

<!-- ─────────── 24 · CMAKE ÇIKTISI ─────────── -->

# CMake çıktısını oku

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Şu iki satırı ara</div>
  <code>Found RapidJSON</code> · <code>Found GStreamer</code>
</div>

- İkisi de görünüyorsa doğru yoldasın
- Görünmüyorsa 2.15'teki paketler eksik → kur, `build` klasörünü
  **sil**, baştan derle

<!-- KOMUT -->
```bash
export GZ_VERSION=harmonic   # unutulursa cmake yanlış sürümü arar
```

---

<!-- ─────────── 25 · YOL TUZAĞI ─────────── -->

# Tuzak — dizin mi, dosya mı?

<!-- KOMUT -->
```bash
find /usr/local -name '*ArduPilotPlugin*' 2>/dev/null
# /usr/local/lib/ardupilot_gazebo/libArduPilotPlugin.so
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Yola DİZİNİ ekle, dosyayı değil</div>
  Doğru → <code>/usr/local/lib/ardupilot_gazebo</code><br>
  Yanlış → <code>.../ardupilot_gazebo/libArduPilotPlugin.so</code>
</div>

Yanlış yazarsan Gazebo `ArduPilotPlugin not found` der.

---

<!-- ═══════ 2.17 · MODELLER ═══════ -->
<!-- ─────────── 26 · SITL_MODELS ─────────── -->

# Uçak modelleri

<!-- KOMUT -->
```bash
cd ~
git clone https://github.com/ArduPilot/SITL_Models.git
```

Bu depo, Gazebo'da kullanılacak **3B modelleri**, fizik ayarlarını
ve dünya dosyalarını içeriyor.

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Model nedir?</div>
  Uçağın görünüşü (mesh), ağırlığı, kanat alanı, motor gücü —
  Gazebo'nun fiziği hesaplamak için ihtiyaç duyduğu her şey.
</div>

---

<!-- ─────────── 27 · UAV_TRANSFER ─────────── -->

# Kurs deposunu indir

Bundan sonraki adımlarda **kursa özel** dosyalar lazım. Hepsi tek depoda:

<!-- KOMUT -->
```bash
cd ~
git clone https://github.com/yagizyungul/iha-otonom-kurs.git
```

- `kurulum/UAV_TRANSFER.tar.gz` → kursun **üç uçağı**
- `kurulum/create_satellite_ground.py` → uydu görüntülü zemin
- `kod/` → sonraki bölümlerin Python dosyaları

---

<!-- ─────────── + · DEPODA NE VAR ─────────── -->

# Neden ayrı bir depo?

<div class="ky-ikili">

<div>

ArduPilot ve SITL_Models **resmî** depolar — herkese açık, genel amaçlı.

Kursun üç uçağı, dünya dosyası ve yardımcı script'ler orada **yok**.
Onları biz hazırladık, kendi depomuzda duruyorlar.

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Bir kez indir, hep kullan</div>
  Bu depoyu bir daha indirmeyeceksin. Bölüm 6, 7 ve 8'in kodları da
  burada. Güncelleme gelirse <code>git pull</code> yeter.
</div>

</div>

---

<!-- ─────────── + · ÜÇ UÇAĞI KUR ─────────── -->

# Üç uçağı kur

<!-- KOMUT -->
```bash
cp ~/iha-otonom-kurs/kurulum/UAV_TRANSFER.tar.gz ~/
cd ~ && tar -xzf UAV_TRANSFER.tar.gz
cd ~/UAV_TRANSFER
chmod +x install.sh
./install.sh
```

- `cp` → paketi depodan **ev dizinine** kopyalar
- `tar -xzf` → arşivi **açar**
- `chmod +x` → script'e **çalıştırma izni** verir

---

<!-- ─────────── + · ÜÇ UÇAK KİM ─────────── -->

# AV1, AV2 ve YEM

<div class="ky-kartlar ky-kartlar--kisa">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>AV1</strong><br>
      Ana uçağımız. Bölüm 6'da bunu Python'la uçuracağız.
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>AV2</strong><br>
      İkinci avcı. Kameralı uçak, Bölüm 7'de görüntü işleyeceğiz.
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>YEM</strong><br>
      Hedef uçak. Takip senaryolarında peşine düşeceğiz.
    </div>
  </div>

</div>

---

<!-- ─────────── 28 · UYDU HARİTASI ─────────── -->

# Uydu görüntülü zemin

<!-- KOMUT -->
```bash
pip3 install --break-system-packages Pillow
mkdir -p ~/SITL_Models/Gazebo/scripts
cp ~/iha-otonom-kurs/kurulum/create_satellite_ground.py \
   ~/SITL_Models/Gazebo/scripts/
cd ~/SITL_Models/Gazebo/scripts
python3 create_satellite_ground.py
```

İnternet gerekiyor. Yoksa bu adımı atla — Gazebo düz zeminle açılır,
simülasyon **aynı şekilde çalışır**.

---

<!-- ─────────── + · SCRIPT NE YAPIYOR ─────────── -->

# Bu script ne yapıyor?

<div class="ky-ikili">

<div>

`create_satellite_ground.py` üç iş yapıyor:

- Belirlenen koordinatın **uydu karolarını indiriyor**
- Karoları tek bir büyük görüntüde **birleştiriyor**
- Gazebo'nun zemin dokusu olarak **kaydediyor**

Sonuç: uçak gri bir düzlemin değil, gerçek arazinin üstünde uçuyor.

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Bu dosya SITL_Models'te YOK</div>
  Kursa özel bir script; <strong>kurs deposunda</strong> geliyor:
  <code>iha-otonom-kurs/kurulum/</code>. Onun için önce kopyalıyoruz.
</div>

</div>

---

<!-- ═══════ 2.18 · ORTAM DEĞİŞKENLERİ ═══════ -->
<!-- ─────────── 29 · NEDEN GEREKLİ ─────────── -->

# Gazebo modelleri nerede arasın?

<div class="ky-ikili">

<div>

Gazebo, eklentileri ve modelleri **kendi bilmediği** dizinlerde
aramaz. İki değişkenle yerlerini söylüyoruz.

- `GZ_SIM_SYSTEM_PLUGIN_PATH` → eklentiler
- `GZ_SIM_RESOURCE_PATH` → modeller ve dünyalar

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Terminalde yazmak yetmez</div>
  <code>export</code> sadece <strong>o terminal</strong> için geçerli.
  Kalıcı olması için <code>~/.bashrc</code>'ye yazacağız.
</div>

</div>

---
class: kod-sm
---

<!-- ─────────── 30 · BASHRC ─────────── -->

# `~/.bashrc`'ye ekle

<!-- KOMUT -->
```bash
nano ~/.bashrc
```

Dosyanın **en sonuna** üç satır:

<!-- KOMUT -->
```bash
export GZ_VERSION=harmonic
export GZ_SIM_SYSTEM_PLUGIN_PATH=/usr/local/lib/ardupilot_gazebo:$GZ_SIM_SYSTEM_PLUGIN_PATH
export GZ_SIM_RESOURCE_PATH=$HOME/SITL_Models/Gazebo/models:$HOME/SITL_Models/Gazebo/worlds:$GZ_SIM_RESOURCE_PATH
```

Kaydet: **Ctrl+O** → Enter → **Ctrl+X**

---

<!-- ─────────── 31 · UYGULA VE DOĞRULA ─────────── -->

# Uygula ve doğrula

<!-- KOMUT -->
```bash
source ~/.bashrc
echo $GZ_SIM_SYSTEM_PLUGIN_PATH
echo $GZ_SIM_RESOURCE_PATH
```

İkisi de **dolu** dönmeli.

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Sondaki <code>:$GZ_...</code> ne işe yarıyor?</div>
  Değişkenin <strong>eski değerini koruyor</strong>. Olmazsa başka bir
  programın eklediği yolları silersin.
</div>

---
class: kod-sm
---

<!-- ─────────── 32 · PYTHON PAKETLERİ ─────────── -->

# Python paketleri

<!-- KOMUT -->
```bash
pip3 install --break-system-packages \
  pymavlink opencv-python opencv-contrib-python \
  ultralytics dronekit pyzbar Pillow flask geopy
```

- **pymavlink** → Bölüm 6, uçağı Python'dan kontrol
- **opencv / ultralytics** → Bölüm 7, kamera ve YOLO
- **flask / geopy** → Bölüm 8, sunucu senaryosu

Hepsini şimdi kuruyoruz ki ilerideki bölümlerde kurulumla uğraşma.

---

<!-- ─────────── 33 · SON DOĞRULAMA ─────────── -->

# Kurulum kontrol listesi

<!-- KOMUT -->
```bash
ls ~/ardupilot/build/sitl/bin/arduplane   # ArduPilot
gz sim --version                          # Gazebo
find /usr/local -name '*ArduPilotPlugin*' # köprü
ls ~/SITL_Models/Gazebo/worlds            # modeller
echo $GZ_SIM_RESOURCE_PATH                # yollar
python3 -c "import pymavlink; print('ok')"
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Altısı da yanıt veriyorsa</div>
  Kurulum bitti. <strong>Bölüm 3'te ilk uçuşu</strong> yapacağız.
</div>

---

<!-- ─────────── + · DUMAN TESTİ 1 ─────────── -->

# Hepsi birlikte çalışıyor mu?

Parçaları tek tek test ettik. Şimdi **ikisini birden** çalıştırıp
konuştuklarını görelim. Uçurmayacağız — sadece bağlantıyı doğrulayacağız.

**Terminal 1 — dünyayı aç:**

<!-- KOMUT -->
```bash
gz sim -v4 -r ~/SITL_Models/Gazebo/worlds/dual_vtail_runway_3uav.sdf
```

Pistte üç uçak görünmeli. Görünmüyorsa `GZ_SIM_RESOURCE_PATH` eksik.

---
class: kod-sm
---

<!-- ─────────── + · DUMAN TESTİ 2 ─────────── -->


# Uçağı dünyaya bağla

**Terminal 2 — SITL'i başlat:**

<!-- KOMUT -->
```bash
cd ~/ardupilot && sim_vehicle.py -v ArduPlane -f JSON --model JSON \
  --add-param-file=$HOME/SITL_Models/Gazebo/config/mini_talon_vtail.param \
  --console --map -I0
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Aradığımız şey</div>
  Konsolda irtifa ve hız değerlerinin akmaya başlaması. Akıyorsa
  <strong>köprü çalışıyor</strong>, kurulumun tamamı doğru.
  Kapatmak için iki terminalde de Ctrl+C.
</div>

---

<!-- ─────────── + · KAPANIŞ ─────────── -->

# Kurulum bitti

<div class="ky-ikili">

<div>

Boş bir Ubuntu ile başladın. Şimdi elinde:

- Çalışan bir **otopilot** yazılımı
- **3B simülasyon** ortamı
- İkisini bağlayan **köprü**
- Uçak **modelleri** ve dünya

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b2-gazebo-uc-ucak.png" alt="Üç uçak havada">
  </div>
  <figcaption>Bölüm 3'te bunu birlikte uçuracağız</figcaption>
</figure>

</div>

