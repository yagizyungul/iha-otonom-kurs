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
     BÖLÜM 2 — ORTAM KURULUMU · 18 ders · 56 slayt · ~163 dakika

     İKİ YARI:
       2A (2.1–2.8)  Ubuntu'yu kurmak      slayt 1-44
       2B (2.9–2.18) Yazılımı kurmak       slayt 45-56

     2A yeni eklendi: öğrencilerin çoğu işletim sistemi kurulumunda
     bırakıyor. Dört yol var, öğrenci birini seçip diğerlerini atlıyor.
     Slayt 8 bu yönlendirmeyi yapıyor — o slayt bölümün pusulası.

     2B TERMİNAL ağırlıklı. Slaytlar sadece noktalama işareti:
     her dersin başında "ne yapacağız", tuzaklarda uyarı, sonda özet.
     Komutların tamamı çekim metninde (yeşil kutular).

     Ders → slayt eşlemesi:
       2.1  Hangi yol senin için?     slayt 1-8
       2.2  Diskini anlamak           slayt 9-15
       2.3  Windows'ta yer açma       slayt 16-20
       2.4  ISO ve USB                slayt 21-24
       2.5  Dual boot kurulumu        slayt 25-35
       2.6  Sanal makine              slayt 36-39
       2.7  MacBook                   slayt 40-42
       2.8  İlk açılış                slayt 43-44
       2.9  Terminal temel            slayt 45-46
       2.10 Sistem paketleri          slayt 47
       2.11 ArduPilot derleme         slayt 48
       2.12 NumPy tuzağı              slayt 49
       2.13 İlk SITL testi            (slayt yok — terminal)
       2.14 Gazebo Harmonic           slayt 50
       2.15 Kütüphaneler/GStreamer    slayt 51
       2.16 Plugin derleme            slayt 52
       2.17 Modeller                  slayt 53
       2.18 Ortam değişkenleri        slayt 54-55

     KAYNAKTAN DOĞRULANDI (Ubuntu 22.04.5 · 3 Ağustos 2026):
       - MAVProxy 1.8.74 + numpy 2.2.6 SORUNSUZ. Rehberdeki
         "numpy<2 KRİTİK" adımı artık geçersiz.
       - Taze 22.04'te pip 22.0.2 var, --break-system-packages
         bayrağı YOK. O bayrak 24.04 (PEP 668) için.
       - Plugin yolu: /usr/local/lib/ardupilot_gazebo/
       - Gazebo Sim 8.12.0 (Harmonic), jammy deposundan

     2A İÇİN ÇEKİM NOTU: bu derslerin dördü Ubuntu'nun DIŞINDA
     geçiyor (Windows, BIOS, kurulum sihirbazı). Müfredat §6.1'e bak.

     TAŞMA: her slayt tek ana blok + en fazla iki satırlık tek kutu.
     Kutudan sonra cümle EKLEME — taşma denetimi oradan patlıyor.
     ═══════════════════════════════════════════════════════════ -->

<!-- ─────────── 1 · KAPAK ─────────── -->

<div class="ky-kapak-serit"></div>

# Ortam Kurulumu

<div class="ky-kapak-alt">

Bölüm 2 · Boş bilgisayardan çalışan simülasyona

</div>

---

<!-- ─────────── 2 · BU BÖLÜMDE ─────────── -->

# Bu bölümde

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">2A</div>
    <div class="ky-kart__govde">
      <strong>Ubuntu'yu kurmak</strong><br>
      Disk, USB, dual boot, sanal makine, Mac.
      Linux'un yoksa buradan başla
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">2B</div>
    <div class="ky-kart__govde">
      <strong>Yazılımı kurmak</strong><br>
      ArduPilot, Gazebo, köprü, modeller.
      Ubuntu'n varsa doğrudan buraya geç
    </div>
  </div>

</div>

---

<!-- ─────────── 3 · BÖLÜM NEDEN UZUN ─────────── -->

# Bu bölüm neden bu kadar uzun?

- Kursun **en uzun** bölümü — 18 ders
- Çünkü öğrencilerin çoğu tam **burada** bırakıyor
- Her tuzak tek tek gösterilecek
- Hiçbiri "kolayca kurulur" diye geçilmeyecek

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Hepsini izlemeyeceksin</div>
  2A'da dört ayrı yol var; sen yalnızca kendi yolunu izleyeceksin.
</div>

---

<!-- ═══════ 2.1 · HANGİ YOL SENİN İÇİN? ═══════ -->
<!-- ─────────── 4 · DÖRT YOL ─────────── -->

# Ubuntu'ya dört yol

<div class="ky-kartlar" style="--n:4">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>Dual boot</strong><br>
      Diski bölüp yanına kur. Referans yol
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Sanal makine</strong><br>
      Windows içinde pencere. Kolay ama yavaş
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Harici SSD</strong><br>
      İç diske hiç dokunmaz
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">4</div>
    <div class="ky-kart__govde">
      <strong>Mac</strong><br>
      Apple Silicon ayrı bir dünya
    </div>
  </div>

</div>

---

<!-- ─────────── 5 · KARŞILAŞTIRMA ─────────── -->

# Üçü yan yana

```
               Dual boot   Sanal mak.   Harici SSD
--------------------------------------------------
Gazebo hızı    tam         yavaş        tam
Kurulum riski  orta        yok          düşük
Geri dönüş     zor         sil, bitti   kabloyu çek
Windows'a etki bölünür     yok          yok
```

Sanal makinenin tek gerçek sınırı Gazebo'nun 3B penceresi — yani **2.14 ve sonrası**.

---

<!-- ─────────── 6 · KARAR AĞACI ─────────── -->

# Hangisini seçmelisin?

```
Mac kullanıyorum             ->  Mac yolu
Diskimi bölmeye çekinmiyorum ->  dual boot
Harici SSD alabilirim        ->  harici SSD
Diske hiç dokunmak istemem   ->  sanal makine
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Kararsızsan: dual boot</div>
  Tek seferlik zahmet, sonrasında tam performans.
</div>

---

<!-- ─────────── 7 · DONANIM ─────────── -->

# Donanım yeterli mi?

<div class="ky-ikili">

<div>

- **RAM** — 8 GB çalışır, **16 GB** rahat eder
- **Disk** — en az **80 GB**, tercihen 150 GB
- **İşlemci** — son 8 yılın i5/Ryzen 5'i yeter
- **Ekran kartı** — ayrı kart şart değil

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Üç uçak aynı anda</div>
  Bölüm 3'te üç SITL + Gazebo birlikte çalışacak.
</div>

</div>

---

<!-- ─────────── 8 · BÖLÜM PUSULASI ─────────── -->

# Bundan sonra ne izleyeceksin

- **Herkes** → 2.2 Diskini anlamak
- **Dual boot** seçtiysen → 2.3, 2.4, 2.5, 2.8
- **Harici SSD** seçtiysen → 2.4, 2.5, 2.8
- **Sanal makine** seçtiysen → 2.6, 2.8
- **Mac** kullanıyorsan → 2.7
- **Ubuntu'n zaten varsa** → doğrudan **2.9**

Seçmediğin yolları atla; hiçbiri sonrakinin ön koşulu değil.

---

<!-- ═══════ 2.2 · DİSKİNİ ANLAMAK ═══════ -->
<!-- ─────────── 9 · DİSK VE BÖLÜM ─────────── -->

# Disk, bölüm, dosya sistemi

<div class="ky-ikili">

<div>

- **Disk** — fiziksel donanım, tek parça
- **Bölüm** — diskin mantıksal dilimi
- **Dosya sistemi** — bölümün içindeki düzen

Windows **NTFS**, Linux **ext4** kullanır.

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">"C: ve D: iki disk mi?"</div>
  Genelde hayır — aynı diskin iki bölümü olabilir.
</div>

</div>

---

<!-- ─────────── 10 · DİSKTE NE VAR ─────────── -->

# Windows'lu bir diskte ne var?

```
nvme0n1p1   EFI          512 MB   açılış dosyaları
nvme0n1p2   MSR           16 MB   Windows ayırdı
nvme0n1p3   C: (NTFS)    900 GB   Windows ve verilerin
nvme0n1p4   Recovery     600 MB   Windows kurtarma
```

Dört bölüm görüp korkma — üçü sistemin, seninki **C:**.

---

<!-- ─────────── 11 · LİNUX NEREYE ─────────── -->

# Linux nereye girecek?

Yeni bir bölüme. Onu **C:'yi küçülterek** açacağız — C:'nin
içindekilere dokunmadan.

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Küçültmek silmek değil</div>
  Veriler diskin başında toplanır, sonundaki boşluk serbest kalır.
</div>

---

<!-- ─────────── 12 · UEFI / GPT ─────────── -->

# UEFI ve GPT

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">✓</div>
    <div class="ky-kart__govde">
      <strong>UEFI + GPT</strong><br>
      2012 sonrası her bilgisayar. EFI bölümü Windows ve
      Linux tarafından ortak kullanılır
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">◷</div>
    <div class="ky-kart__govde">
      <strong>Legacy BIOS + MBR</strong><br>
      Eski sistemler, en fazla 4 birincil bölüm.
      Kursta bu yolu anlatmıyoruz
    </div>
  </div>

</div>

Windows UEFI kuruluysa Ubuntu da **UEFI** kurulmalı.

---

<!-- ─────────── 13 · GRUB ─────────── -->

# Açılışta ne oluyor?

```mermaid {theme: 'base', scale: 0.72, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '19px', fontFamily: 'Figtree'}}
flowchart LR
  A[Güç] --> B[UEFI<br>ürün yazılımı]
  B --> C[EFI bölümü]
  C --> D[GRUB menüsü]
  D --> E[Ubuntu]
  D --> F[Windows]
  style D fill:#ffffff,stroke:#6e4bf0,stroke-width:3px
  style E fill:#ffffff,stroke:#00a6a0,stroke-width:2px
  style F fill:#ffffff,stroke:#1257f0,stroke-width:2px
```

**GRUB** — açılışta hangi sistemi istediğini soran menü.

---

<!-- ─────────── 14 · KAÇ BÖLÜM ─────────── -->

# Linux kaç bölüm ister?

<div class="ky-ikili">

<div>

- **EFI** — zaten var, **yenisini açma**
- **`/` (kök)** — ext4, her şey burada
- **swap** — isteğe bağlı

Kursta **tek bölüm** açıyoruz: `/`

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Ayrı /home gerekli mi?</div>
  Sunucuda mantıklı, burada değil. Tek bölüm, daha az hata.
</div>

</div>

---

<!-- ─────────── 15 · VERİ KAYBI NEREDE ─────────── -->

# Veri kaybı tam olarak nerede olur?

- Riskli adım kurulum değil, **küçültme** — veriler fiziksel olarak taşınır
- Küçültmeden önce **yedek al**, dizüstüyse **şarjı tak**
- İkinci riskli an: kurulumda **yanlış bölümü seçmek**

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Yedeğin varsa</div>
  En kötü senaryo bir akşam kaybetmektir, verilerini değil.
</div>

---

<!-- ═══════ 2.3 · WINDOWS'TA YER AÇMA ═══════ -->
<!-- ─────────── 16 · PLAN ─────────── -->

# Windows'ta yer açma planı

- **1 ·** BitLocker'ı kapat
- **2 ·** Hızlı başlatma ve hazırda beklet'i kapat
- **3 ·** Disk Yönetimi ile C:'yi küçült
- **4 ·** Açılan alanı **ayrılmamış** bırak

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Neden biçimlendirmiyoruz?</div>
  Ubuntu kurulumu o alanı kendi biçimlendirecek.
</div>

---

<!-- ─────────── 17 · BITLOCKER ─────────── -->

# BitLocker açıksa

- Ayarlar → Gizlilik ve güvenlik → **Cihaz şifrelemesi** → kapat
- Kapatamıyorsan **kurtarma anahtarını yazdır**
- Kurumsal bilgisayarsa BT'ye sormadan devam etme

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Şifreli diski küçültmek riskli</div>
  Disk düzeni değişince Windows kurtarma anahtarı isteyebilir.
</div>

---

<!-- ─────────── 18 · HIZLI BAŞLATMA ─────────── -->

# Hızlı başlatmayı kapat

Windows "kapan" dediğinde tam kapanmıyor; diski **kilitli** bırakıyor.

```
powercfg /h off
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Kapatmazsan</div>
  Linux, Windows bölümünü salt okunur bağlar ya da hiç bağlamaz.
</div>

---

<!-- ─────────── 19 · KÜÇÜLTME ─────────── -->

# Disk Yönetimi ile küçültme

```
Win + X  →  Disk Yönetimi       (diskmgmt.msc)
C: sağ tık  →  Birimi Küçült
Küçültülecek alan (MB):  150000
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Sonuç ne görünmeli?</div>
  C:'nin sağında siyah çubuklu <strong>"Ayrılmamış"</strong> alan.
</div>

---

<!-- ─────────── 20 · AZ YER VERİYOR ─────────── -->

# "Windows bu kadar yer vermiyor"

<div class="ky-ikili">

<div>

Diskte 500 GB boş ama Windows 40 GB izin veriyor. Sebep:
**taşınamaz dosyalar** — sayfa dosyası, sistem geri yükleme.

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Sırayla dene</div>
  1 · <code>powercfg /h off</code><br>
  2 · Sistem korumasını kapat<br>
  3 · Yeniden başlat, tekrar dene<br>
  4 · Olmuyorsa <strong>GParted</strong>
</div>

</div>

---

<!-- ═══════ 2.4 · ISO VE USB ═══════ -->
<!-- ─────────── 21 · ISO ─────────── -->

# Doğru ISO'yu indir

```
releases.ubuntu.com/22.04/
ubuntu-22.04.5-desktop-amd64.iso    ~4.7 GB
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Üç yanlış indirme</div>
  <strong>server</strong> arayüzsüz · <strong>24.04</strong> referans değil ·
  <strong>arm64</strong> PC'de açılmaz
</div>

---

<!-- ─────────── 22 · SHA256 ─────────── -->

# İndirdiğin dosya sağlam mı?

```
certutil -hashfile ubuntu-22.04.5-desktop-amd64.iso SHA256
```

Çıkan sayıyı `SHA256SUMS` dosyasındakiyle karşılaştır.

<div class="ky-kutu">
  <div class="ky-kutu__baslik">İki dakikanı neden ayırıyorsun?</div>
  Yarım inen ISO kurulumun <strong>ortasında</strong> hata verir.
</div>

---

<!-- ─────────── 23 · USB YAZMA ─────────── -->

# USB'ye yazmak

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">W</div>
    <div class="ky-kart__govde">
      <strong>Rufus</strong> — Windows<br>
      Bölüm düzeni <strong>GPT</strong>,
      hedef sistem <strong>UEFI</strong>
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">M</div>
    <div class="ky-kart__govde">
      <strong>balenaEtcher</strong><br>
      Windows, macOS, Linux'ta aynı.
      Seç, seç, yaz
    </div>
  </div>

</div>

8 GB'lık **boş** bir USB kullan — içindekiler tamamen silinir.

---

<!-- ─────────── 24 · USB TUZAKLARI ─────────── -->

# USB açılmıyorsa

- **USB 2.0 portu** dene — bazı kartlar 3.0'da tanımıyor
- Yazma bitince Windows "biçimlendir" derse **iptal et**
- Ucuz/eski USB'ler sessizce bozuk yazar
- Boot menüsünde **UEFI: USB** yazan satırı seç

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Harici SSD yolundaysan</div>
  Kurulum USB'si yine gerekli; fark, hedef diskin SSD olması.
</div>

---

<!-- ═══════ 2.5 · DUAL BOOT KURULUMU ═══════ -->
<!-- ─────────── 25 · KONTROL LİSTESİ ─────────── -->

# Kuruluma başlamadan

- Yedek alındı
- BitLocker ve hızlı başlatma kapalı
- Ayrılmamış alan hazır — en az 80 GB
- USB yazıldı, şarj takılı, internet var

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Dördü de tamamsa</div>
  Kurulum sıkıcı derecede sorunsuz geçer.
</div>

---

<!-- ─────────── 26 · BIOS'A GİRMEK ─────────── -->

# BIOS/UEFI'ye girmek

```
ASUS, MSI, Gigabyte      Del
Dell, Lenovo, Acer       F2
HP                       F10   (menü: Esc)
Casper, Monster          F2 / Del
```

Açılışta **hemen** basılır; Windows logosu geldiyse geç kaldın.

---

<!-- ─────────── 27 · TUŞU TUTTURAMIYORSAN ─────────── -->

# Tuşu tutturamıyorsan

```
Shift basılı tut + Yeniden Başlat
  → Sorun Giderme
  → Gelişmiş Seçenekler
  → UEFI Ürün Yazılımı Ayarları
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Bu yol daha güvenilir</div>
  Zamanlama gerektirmiyor, hızlı başlatma açıkken de çalışıyor.
</div>

---

<!-- ─────────── 28 · İKİ AYAR ─────────── -->

# BIOS'ta iki ayar

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>Secure Boot</strong><br>
      Ubuntu imzalı, açık kalabilir.
      Kurulum takılırsa geçici kapat
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>RAID / Intel RST</strong><br>
      Açıksa Ubuntu diski <strong>hiç görmez</strong>.
      AHCI'ye çevrilmeli
    </div>
  </div>

</div>

RST'yi doğrudan çevirme — Windows açılmaz hale gelir, sırası derste.

---

<!-- ─────────── 29 · TRY UBUNTU ─────────── -->

# Önce "Try Ubuntu"

USB'den açılınca **kurmadan** dene:

- Wi-Fi çalışıyor mu
- Ekran çözünürlüğü doğru mu
- Ses, klavye, touchpad

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Beş dakikanı burada harca</div>
  Bu ekranda çalışmayan şey kurulumdan sonra da çalışmaz.
</div>

---

<!-- ─────────── 30 · SİHİRBAZ ─────────── -->

# Kurulum sihirbazı

- **Dil** — İngilizce, **klavye** — Turkish Q
- **Kurulum türü** — Normal
- **Güncellemeler** — kapalı bırak
- **Üçüncü taraf yazılım** — **işaretle**

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Neden İngilizce arayüz?</div>
  Hata mesajını aratınca çözüm bulman kat kat kolay olur.
</div>

---

<!-- ─────────── 31 · KRİTİK EKRAN ─────────── -->

# Kritik ekran: kurulum türü

<div class="ky-kartlar" style="--n:3">

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">✗</div>
    <div class="ky-kart__govde">
      <strong>Erase disk</strong><br>
      Diskteki her şeyi siler. Windows dahil
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">~</div>
    <div class="ky-kart__govde">
      <strong>Install alongside</strong><br>
      Çalışır ama ne yaptığını göstermez
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">✓</div>
    <div class="ky-kart__govde">
      <strong>Something else</strong><br>
      Bizim seçeceğimiz. Her bölümü sen belirlersin
    </div>
  </div>

</div>

---

<!-- ─────────── 32 · BÖLÜM TABLOSU ─────────── -->

# "Something else" ekranı

```
/dev/nvme0n1p1  efi    512M           ← DOKUNMA
/dev/nvme0n1p3  ntfs   900G  Windows  ← DOKUNMA
serbest alan           150G           ← BURAYA
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Tek satır seçeceksin</div>
  "serbest alan" / "free space" yazan satır. Başkasına dokunma.
</div>

---

<!-- ─────────── 33 · BÖLÜM OLUŞTURMA ─────────── -->

# Yeni bölümü oluşturmak

Serbest alanı seç → **+** → üç değer:

```
Boyut:            hepsi
Türü:             Ext4
Bağlama noktası:  /
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Biçimlendir kutucuğu</div>
  Yalnızca yeni açtığın bölümde işaretli olsun.
</div>

---

<!-- ─────────── 34 · BOOTLOADER ─────────── -->

# Bootloader nereye?

```
Device for boot loader installation:
  /dev/nvme0n1        ← DİSKİN KENDİSİ
  /dev/nvme0n1p1      ✗ bölüm değil
```

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Install Now'dan sonra özeti oku</div>
  Yalnız yeni bölümün adı yazmalı. Windows görürsen geri dön.
</div>

---

<!-- ─────────── 35 · GRUB MENÜSÜ ─────────── -->

# İlk açılış: GRUB menüsü

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Menü gelmiyor, Windows açılıyorsa</div>
  BIOS'ta önyükleme sırası bozuktur — <strong>ubuntu</strong> en üste.
</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Menüde Windows yoksa</div>
  <code>sudo os-prober</code> ve <code>sudo update-grub</code> çalıştır.
</div>

---

<!-- ═══════ 2.6 · SANAL MAKİNE ═══════ -->
<!-- ─────────── 36 · VM NE ZAMAN ─────────── -->

# Sanal makine: ne zaman mantıklı?

<div class="ky-ikili">

<div>

**Mantıklı:** Linux'u ilk kez deniyorsan, diskine dokunmak
istemiyorsan, bir haftada vazgeçebilmek istiyorsan.

**Mantıksız:** Gazebo'yu akıcı çalıştırmak, üç uçağı birlikte uçurmak.

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Önermiyoruz ama gösteriyoruz</div>
  Çoğu öğrenci buradan başlıyor. 2.9–2.13 VM'de sorunsuz.
</div>

</div>

---

<!-- ─────────── 37 · VM AYARLARI ─────────── -->

# VirtualBox: makine ayarları

```
Bellek          8192 MB   (en az 4096)
İşlemci         4 çekirdek
Disk            80 GB     dinamik
EFI             Etkin
Ekran belleği   128 MB
3B hızlandırma  Etkin
```

Ana makineye yarısından fazlasını verme — ikisi birden yavaşlar.

---

<!-- ─────────── 38 · VM KURULUM ─────────── -->

# VM içinde kurulum

Aynı sihirbaz, tek farkla: disk boş olduğu için
**"Erase disk and install Ubuntu"** seçilebilir.

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Burada silinecek bir şey yok</div>
  Dual boot'ta yasak olan seçenek, burada doğru seçenek.
</div>

Kurulumdan sonra **Guest Additions**: tam ekran, ortak pano.

---

<!-- ─────────── 39 · VM SINIRI ─────────── -->

# VM'in duvara toslayacağı yer

- Gazebo'nun görselleştiricisi **OpenGL 3.3+** istiyor
- VirtualBox'ın sanal ekran kartı bunu tam veremiyor
- Belirti: `gz sim` açılır, pencere **siyah** kalır
- Kurtarma: yazılımsal render — çalışır ama çok yavaş

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Geçerli bir plan</div>
  Terminal derslerini VM'de bitir, Gazebo için gerçek kuruluma geç.
</div>

---

<!-- ═══════ 2.7 · MAC ═══════ -->
<!-- ─────────── 40 · HANGİ MAC ─────────── -->

# Mac'inde hangi işlemci var?

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">Intel</div>
    <div class="ky-kart__govde">
      <strong>2020 ve öncesi</strong><br>
      PC gibi davranır. Bu bölümün geri kalanı sana da uyar
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">M</div>
    <div class="ky-kart__govde">
      <strong>Apple Silicon</strong><br>
      M1–M4. Farklı işlemci mimarisi (ARM), ayrı bir dünya
    </div>
  </div>

</div>

Menü çubuğu → Bu Mac Hakkında → **Yonga** satırı.

---

<!-- ─────────── 41 · ASAHI ─────────── -->

# Apple Silicon: Asahi Linux

**asahilinux.org** — Apple Silicon'a çıplak donanım Linux kuran proje.

- Resmî dağıtımı **Fedora Asahi Remix**
- Ubuntu isteyenler için topluluk projesi: **ubuntuasahi.org**
- macOS silinmez, yanına kurulur

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Kursun desteklediği yol değil</div>
  Referans sistem x86 Ubuntu 22.04; sorunları kendin çözeceksin.
</div>

---

<!-- ─────────── 42 · MAC ÖNERİ ─────────── -->

# Mac kullanıcısına önerim

<div class="ky-kartlar" style="--n:3">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>UTM ile sanal makine</strong><br>
      Ücretsiz, arm64 Ubuntu 22.04. En az sürtünme
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Ayrı bir PC</strong><br>
      İkinci el bir dizüstü, kursun referans ortamı
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Asahi</strong><br>
      En iyi performans, en çok uğraş
    </div>
  </div>

</div>

Ciddi ilerleyeceksen **2**, hemen başlamak istiyorsan **1**.

---

<!-- ═══════ 2.8 · İLK AÇILIŞ ═══════ -->
<!-- ─────────── 43 · İLK AÇILIŞ ─────────── -->

# Ubuntu kuruldu — ilk beş dakika

- Sistem güncellemesi
- Ekran kartı sürücüsü (NVIDIA varsa)
- Türkçe klavye ve dil desteği
- Ekran kilidi ve uykuyu kapat

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Sürücüler nerede?</div>
  Software &amp; Updates → <strong>Additional Drivers</strong>
</div>

---

<!-- ─────────── 44 · KURULUM DOĞRULAMA ─────────── -->

# Kurulum doğru mu?

```
lsb_release -a      # 22.04 yazmalı
free -h             # RAM görünüyor mu
df -h /             # ayırdığın alan burada mı
uname -m            # x86_64
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Dördü de beklediğin gibiyse</div>
  İşletim sistemi tarafı bitti. Bundan sonrası herkes için aynı.
</div>

---

<!-- ═══════ 2B · YAZILIM KURULUMU ═══════ -->
<!-- ─────────── 45 · KURULUM SIRASI ─────────── -->

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

<!-- ─────────── 46 · 2.9 · TERMİNAL ─────────── -->

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

<!-- ─────────── 47 · 2.10 · NE KURUYORUZ ─────────── -->

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

<!-- ─────────── 48 · 2.11 · ARDUPILOT ─────────── -->

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

<!-- ─────────── 49 · 2.12 · TUZAK 1 ─────────── -->

# Tuzak 1 — harita penceresi açılmıyor

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">AttributeError: _ARRAY_API not found</div>
  MAVProxy'nin konsol ve harita pencereleri açılmaz.
</div>

- **Sebep:** derlenmiş modüller NumPy'ın **farklı sürümüne** göre kurulmuş
- **Çözüm:** MAVProxy'yi güncelle — `pip3 install -U MAVProxy`
- Güncel MAVProxy ile NumPy 2 **sorun çıkarmıyor**

---

<!-- ─────────── 50 · 2.14 · GAZEBO ─────────── -->

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

<!-- ─────────── 51 · 2.15 · KÜTÜPHANELER ─────────── -->

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

<!-- ─────────── 52 · 2.16 · TUZAK 2 ─────────── -->

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

<!-- ─────────── 53 · 2.17 · MODELLER ─────────── -->

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

<!-- ─────────── 54 · 2.18 · ORTAM DEĞİŞKENLERİ ─────────── -->

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

<!-- ─────────── 55 · DOĞRULAMA ─────────── -->

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

<!-- ─────────── 56 · ÖZET ─────────── -->

# Bölüm 2 özeti

- Ubuntu **sıfırdan** kuruldu — disk, USB, BIOS, bölümleme
- ArduPilot ve köprü **kaynaktan** derlendi
- Gazebo Harmonic depodan kuruldu
- Üç tuzak: **küçültme**, **NumPy**, **plugin yolu**

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Sonraki bölüm</div>
  <strong>Bölüm 3 — İlk uçuş:</strong> tek uçaktan üç uçağa.
</div>
