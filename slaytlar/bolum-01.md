---
theme: default
title: Bölüm 1 — Temel Kavramlar
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
     BÖLÜM 1 — TEMEL KAVRAMLAR · 5 ders · 28 slayt · ~41 dakika

     1.1 İHA ve otonomi              slayt 1-6     8 dk
     1.2 Uçuş kontrolcüsü            slayt 7-12    8 dk
     1.3 SITL ve Gazebo              slayt 13-17   7 dk
     1.4 Sistem mimarisi             slayt 18-23  10 dk
     1.5 Veri akışı ve portlar       slayt 24-28   8 dk

     KURAL: slayt kesin terimi yazar, benzetmeyi eğitmen SÖZLÜ yapar.
     Slayt metni kısa: madde 3-6 kelime. Uzun anlatım çekim metninde.

     PORTLAR KAYNAKTAN DOĞRULANDI:
       TCP  5760 + 10*instance   (sim_vehicle.py:904)
       FDM  9002 + 10*instance   (sim_vehicle.py:1625, SIM_JSON.h:65)
       MAVLink çıkışı 14550 + 10*instance   (sim_vehicle.py:889)
     ═══════════════════════════════════════════════════════════ -->

<!-- ─────────── 1 · KAPAK ─────────── -->

<div class="ky-kapak-serit"></div>

# Temel Kavramlar

<div class="ky-kapak-alt">

Bölüm 1 · Sistem nasıl çalışıyor?

</div>

---

<!-- ─────────── 2 · BU BÖLÜMDE ─────────── -->

# Bu bölümde

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>İHA</strong> tipleri ve otonomi seviyeleri
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Uçuş kontrolcüsü</strong> ve ArduPilot
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Sistem mimarisi</strong>, veri akışı ve portlar
    </div>
  </div>

</div>

---

<!-- ─────────── 3 · 1.1 · İHA NEDİR ─────────── -->

# İHA nedir?

<div class="ky-ikili">

<div>

**İ**nsansız **H**ava **A**racı — pilotu içinde olmayan hava aracı.

- Yerden **kumandayla** uçurulur
- Ya da **kendi kendine** uçar
- Bu kurs ikincisiyle ilgili

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b1-iha-genel.jpg" alt="Havada uçan sabit kanat İHA">
  </div>
  <figcaption>Pilotu içinde olmayan bir hava aracı</figcaption>
</figure>

</div>

---

<!-- ─────────── YENİ · NEREDE KULLANILIYOR ─────────── -->

# Nerede kullanılıyor?

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">🌾</div>
    <div class="ky-kart__govde">
      <strong>Tarım</strong><br>
      Tarla tarama, ilaçlama, verim haritası
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">🗺</div>
    <div class="ky-kart__govde">
      <strong>Haritalama</strong><br>
      Fotogrametri, maden ve inşaat ölçümü
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">🔍</div>
    <div class="ky-kart__govde">
      <strong>Arama-kurtarma</strong><br>
      Geniş alan tarama, termal kamera
    </div>
  </div>

</div>

Hepsinin ortak noktası: **uzun süre**, **geniş alan**, **tekrarlanabilir rota**.

---

<!-- ─────────── 4 · İKİ TİP ─────────── -->

# İki ana tip

<div class="ky-ikili">

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b1-sabit-kanat.jpg" alt="Sabit kanat model uçak">
  </div>
  <figcaption><strong>Sabit kanat</strong> — uzun menzil, yüksek hız</figcaption>
</figure>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b1-multirotor.jpg" alt="Çok pervaneli multirotor İHA">
  </div>
  <figcaption><strong>Multirotor</strong> — havada durabilir, dikey kalkış</figcaption>
</figure>

</div>

---

<!-- ─────────── 5 · NEDEN SABİT KANAT ─────────── -->

# Bu kursta: sabit kanat

<div class="ky-ikili">

<div>

- **Uçuş süresi** kat kat uzun
- **Menzil** daha geniş
- Yarışmalarda **standart**
- Kontrolü daha **zor** — öğretici

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Kod aynı kalır</div>
  Öğrendiğin MAVLink komutları multirotorda da
  <strong>değişmeden</strong> çalışır.
</div>

</div>

---

<!-- ─────────── YENİ · KARŞILAŞTIRMA ─────────── -->

# Sayılarla karşılaştırma

```
                 Sabit kanat      Multirotor
------------------------------------------------
Uçuş süresi      45–90 dk         15–30 dk
Menzil           on km'ler        birkaç km
Havada durma     yapamaz          yapabilir
Kalkış           pist / fırlatma  dikey
Rüzgâr           daha dayanıklı   daha hassas
```

Değerler tipik sınıflar için; modele göre değişir.

---

<!-- ─────────── 6 · OTONOMİ SEVİYELERİ ─────────── -->

# Otonomi seviyeleri

<div class="ky-kartlar" style="--n:4">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">0</div>
    <div class="ky-kart__govde">
      <strong>Manuel</strong><br>Her şeyi pilot yapar
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>Destekli</strong><br>Otopilot dengede tutar
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Görev</strong><br>Waypoint'leri takip eder
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Otonom</strong><br>Kendi karar verir
    </div>
  </div>

</div>

---

<!-- ─────────── YENİ · KURS NEREYE ─────────── -->

# Bu kurs seni nereye götürüyor?

<div class="ky-ikili">

<div>

- **Bölüm 3–4:** seviye 2 — waypoint takibi
- **Bölüm 6:** seviye 2–3 — kodla kontrol
- **Bölüm 7:** seviye 3 — kameradan karar

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Seviye atlamak kod işi</div>
  Donanım aynı kalıyor. Farkı yaratan, uçağa <strong>ne
  söylediğin</strong>.
</div>

</div>

---

<!-- ─────────── 7 · 1.2 · UÇUŞ KONTROLCÜSÜ ─────────── -->

# Uçuş kontrolcüsü

<div class="ky-ikili">

<div>

Uçağın **beyni**. Sensörleri okur, kontrol yüzeylerini sürer.

- Saniyede **yüzlerce kez** çalışır
- Yazılımı **otopilot** yazılımıdır
- Örnek donanım: **Pixhawk**

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/pixhawk.jpg" alt="Pixhawk uçuş kontrolcüsü">
  </div>
  <figcaption>Pixhawk — yaygın bir uçuş kontrolcüsü</figcaption>
</figure>

</div>

---

<!-- ─────────── 8 · SENSÖRLER ─────────── -->

# İçindeki sensörler

<div class="ky-kartlar" style="--n:4">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">IMU</div>
    <div class="ky-kart__govde">
      İvme ve dönüş hızı<br><strong>Eğim, yalpa</strong>
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">BARO</div>
    <div class="ky-kart__govde">
      Hava basıncı<br><strong>İrtifa</strong>
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">MAG</div>
    <div class="ky-kart__govde">
      Manyetik alan<br><strong>Yön</strong>
    </div>
  </div>

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">GPS</div>
    <div class="ky-kart__govde">
      Uydu sinyali<br><strong>Konum</strong>
    </div>
  </div>

</div>

---

<!-- ─────────── YENİ · SENSÖR FÜZYONU ─────────── -->

# Neden tek sensör yetmez?

<div class="ky-ikili">

<div>

Her sensörün bir zayıflığı var:

- **IMU** hızlı ama **kayar** — hata birikir
- **GPS** kaymaz ama **yavaş** ve kesilebilir
- **Barometre** hava durumundan etkilenir

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Kestirim (EKF)</div>
  Otopilot hepsini birleştirip <strong>tek bir tahmin</strong> üretir.
  Biri kesilirse diğerleri boşluğu doldurur.
</div>

</div>

---

<!-- ─────────── 9 · KONTROL DÖNGÜSÜ ─────────── -->

# Ne yapıyor?

```mermaid {theme: 'base', scale: 1.1, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '20px', fontFamily: 'Figtree'}}
flowchart LR
  A[Sensörleri oku] --> B[Durumu kestir<br>ve karar ver]
  B --> C[Servo ve motoru sür]
  C -.-> A
  style A fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
  style B fill:#ffffff,stroke:#6e4bf0,stroke-width:2px,color:#14171c
  style C fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
```

Bu döngü **saniyede yüzlerce kez** dönüyor.

---

<!-- ─────────── YENİ · UÇUŞ MODU ─────────── -->

# Uçuş modu nedir?

Otopilotun **ne kadar iş üstlendiğini** belirleyen ayar.

```
MANUAL     kumanda doğrudan yüzeylere
STABILIZE  otopilot dengeyi tutar
GUIDED     tek hedefe otonom uçuş
AUTO       yüklü rotayı takip eder
RTL        kalkış noktasına döner
```

Aynı uçak, aynı donanım — sadece **kimin karar verdiği** değişiyor.

---

<!-- ─────────── 10 · ARDUPILOT ─────────── -->

# ArduPilot

<div class="ky-ikili">

<div>

Uçuş kontrolcüsünün üstünde çalışan **açık kaynak** otopilot yazılımı.

- 2007'den beri geliştiriliyor
- Geniş **topluluk** ve dokümantasyon
- Simülasyon desteği **dahili**

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Araç tipine göre sürüm</div>
  <strong>ArduPlane</strong> · sabit kanat<br>
  <strong>ArduCopter</strong> · multirotor<br>
  <strong>ArduRover</strong> · kara aracı<br>
  <strong>ArduSub</strong> · su altı
</div>

</div>

---

<!-- ─────────── 11 · ARDUPILOT vs PX4 ─────────── -->

# ArduPilot mu, PX4 mü?

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">ArduPilot</div>
    <div class="ky-kart__govde">
      Daha çok <strong>hazır özellik</strong>, geniş araç desteği,
      olgun görev sistemi. Hobi ve yarışmada yaygın.
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">PX4</div>
    <div class="ky-kart__govde">
      Daha <strong>modüler</strong> mimari, ROS 2 entegrasyonu güçlü.
      Araştırma ve endüstride yaygın.
    </div>
  </div>

</div>

İkisi de **MAVLink** konuşur — öğreneceğin protokol her ikisinde de aynı.

---

<!-- ─────────── 12 · BU KURSTA ─────────── -->

# Bu kursta ArduPlane

<div class="ky-ikili">

<div>

- Sabit kanat için **ArduPlane**
- Simülasyonu **SITL** ile
- Kod tarafı **pymavlink**

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Neden ArduPilot?</div>
  Simülasyon kurulumu tek komut, dokümantasyonu Türkçe kaynaklarda
  da yaygın, yarışma ekiplerinin çoğu bunu kullanıyor.
</div>

</div>

---

<!-- ─────────── 13 · 1.3 · SITL ─────────── -->

# SITL nedir?

<div class="ky-ikili">

<div>

**S**oftware **I**n **T**he **L**oop — otopilot yazılımı,
uçuş kartı olmadan bilgisayarda çalışır.

- Gerçek uçaktakiyle **aynı** kod
- **Aynı** MAVLink mesajları
- Donanım **gerekmez**

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/sitl_images.jpeg" alt="Çalışan SITL">
  </div>
  <figcaption>Çalışan SITL: telemetri ve harita</figcaption>
</figure>

</div>

---

<!-- ─────────── YENİ · SITL vs HITL ─────────── -->

# SITL'in yakın akrabası: HITL

<div class="ky-kartlar" style="--n:2">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">SITL</div>
    <div class="ky-kart__govde">
      Otopilot <strong>yazılımı</strong> bilgisayarda çalışır.
      Donanım gerekmez. Bu kursun konusu.
    </div>
  </div>

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">HITL</div>
    <div class="ky-kart__govde">
      Otopilot <strong>gerçek kartta</strong> çalışır, sensör verisi
      simülasyondan gelir. Kart gerekir.
    </div>
  </div>

</div>

HITL donanımı da test eder; SITL yazılımı test etmek için yeterli.

---

<!-- ─────────── 14 · SİMÜLASYON ↔ GERÇEK ─────────── -->

# Simülasyonda ne değişir?

<div class="ky-ikili">

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Aynı kalan</div>
  Otopilot yazılımı · uçuş modları · MAVLink mesajları ·
  görev mantığı · <strong>senin kodun</strong>
</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Değişen</div>
  Sensörler <strong>üretilir</strong>, motorlar <strong>hesaplanır</strong>,
  fizik <strong>modeldir</strong>
</div>

</div>

---

<!-- ─────────── 15 · GAZEBO ─────────── -->

# Gazebo ne yapıyor?

<div class="ky-ikili">

<div>

Uçağın içinde uçtuğu **sanal dünya**.

- **Fizik**: yerçekimi, aerodinamik
- **Sensör**: kamera, GPS, IMU
- **Görselleştirme**: 3B görüntü

</div>

<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/b1-gazebo-dunya.jpg" alt="Gazebo'da uydu haritalı pist ve uçaklar">
  </div>
  <figcaption>Gazebo: uydu haritalı zemin ve pistteki uçaklar</figcaption>
</figure>

</div>

---

<!-- ─────────── YENİ · SDF ─────────── -->

# Dünya ve uçak nasıl tanımlanıyor?

<div class="ky-ikili">

<div>

Gazebo her şeyi **`.sdf`** dosyalarından okuyor. SDF bir XML biçimi —
etiketlerle yazılmış düz metin.

- **model.sdf** → uçağın gövdesi, kanadı, motoru
- **world.sdf** → zemin, ışık, içindeki modeller

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Açıp okuyabilirsin</div>
  Kanat açıklığından motor gücüne kadar her değer orada yazıyor.
  Bölüm 3'te bu dosyalara bakacağız.
</div>

</div>

---

<!-- ─────────── 16 · NEYİ SİMÜLE ETMİYOR ───────────
     Dürüstlük slaytı. Simülasyona fazla güvenip sahada sürprizle
     karşılaşmak, bu işte en pahalı hata. -->

# Neyi simüle **etmiyor**?

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Simülasyon gerçeğin yerine geçmez</div>
  Aşağıdakiler modelde ya hiç yok ya da çok basitleştirilmiş.
</div>

- Gövde **titreşimi** ve sensör gürültüsü
- Gerçek **rüzgâr** ve türbülans
- **Donanım arızası**: motor, batarya, bağlantı
- Radyo **menzil** kaybı

---

<!-- ─────────── 17 · İKİSİ BİRLİKTE ─────────── -->

# İkisi birlikte

```mermaid {theme: 'base', scale: 1.35, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '20px', fontFamily: 'Figtree'}}
flowchart LR
  A[Gazebo<br>sanal dünya] -->|sensör verisi| B[ArduPilot SITL<br>beyin]
  B -->|motor komutu| A
  style A fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
  style B fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
```

Gazebo **dünyayı**, SITL **beyni** çalıştırır.

---

<!-- ─────────── 18 · 1.4 · ÜÇ KATMAN ─────────── -->

# Sistemin üç katmanı

<!-- scale 0.9 -> 0.72: dikey zincir üç kutuda uzuyor, tam ölçekte
     alt şeridin altına taşıyor. -->

```mermaid {theme: 'base', scale: 0.72, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '19px', fontFamily: 'Figtree'}}
flowchart TB
  A[1 · Gazebo — fiziksel dünya] --> B[2 · ArduPilot SITL — beyin]
  B --> C[3 · Yer istasyonu — pilot]
  style A fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
  style B fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
  style C fill:#ffffff,stroke:#6e4bf0,stroke-width:2px,color:#14171c
```

Her katman bir alttakiyle **ayrı bir protokolle** konuşuyor.

---

<!-- ─────────── 19 · KATMAN 1 ─────────── -->

# Katman 1 — Gazebo

<div class="ky-ikili">

<div>

- Fizik motorunu çalıştırır
- Sensör verisi **üretir**
- Motor komutunu **uygular**

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">ArduPilotPlugin</div>
  Gazebo ile beyni birbirine bağlayan eklenti. Bölüm 2'de
  kaynaktan derleyeceğiz.
</div>

</div>

---

<!-- ─────────── YENİ · PLUGIN ─────────── -->

# Köprü: ArduPilotPlugin

<div class="ky-ikili">

<div>

Gazebo ile ArduPilot birbirini **tanımıyor**. Aralarında tercüman
gerekiyor.

- Gazebo'dan **sensör** verisini alır
- ArduPilot'a **FDM** ile gönderir
- Gelen **motor komutunu** modele uygular

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Kurulumun en kritik parçası</div>
  Bölüm 2'de bunu kaynaktan derleyeceğiz. Yolu yanlış verilirse
  uçak Gazebo'da <strong>hiç kıpırdamaz</strong>.
</div>

</div>

---

<!-- ─────────── 20 · KATMAN 2 ─────────── -->

# Katman 2 — ArduPilot SITL

<div class="ky-ikili">

<div>

- Sensör verisini **okur**
- Uçuş algoritmasını **çalıştırır**
- Motor komutu **üretir**

</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Kritik nokta</div>
  Bu katmandaki yazılım, gerçek Pixhawk'ta çalışanın
  <strong>aynısı</strong>.
</div>

</div>

---

<!-- ─────────── 21 · KATMAN 3 ─────────── -->

# Katman 3 — Yer istasyonu

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">⌨</div>
    <div class="ky-kart__govde">
      <strong>MAVProxy</strong><br>
      Terminalden komut, SITL ile birlikte açılır
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">🗺</div>
    <div class="ky-kart__govde">
      <strong>Mission Planner</strong><br>
      Görsel arayüz, waypoint planlama
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">🐍</div>
    <div class="ky-kart__govde">
      <strong>Python</strong><br>
      Senin kodun — Bölüm 6'nın konusu
    </div>
  </div>

</div>

---

<!-- ─────────── 22 · KÖPRÜ ─────────── -->

# Katmanlar nasıl bağlanıyor?

```mermaid {theme: 'base', scale: 1.2, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '19px', fontFamily: 'Figtree'}}
flowchart LR
  A[Gazebo] <-->|FDM<br>UDP 9002| B[ArduPilot SITL]
  B <-->|MAVLink<br>UDP 14550| C[Yer istasyonu]
  style A fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
  style B fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
  style C fill:#ffffff,stroke:#6e4bf0,stroke-width:2px,color:#14171c
```

İki farklı protokol: içeride **FDM**, dışarıda **MAVLink**.

---

<!-- ─────────── 23 · DÖNGÜ ─────────── -->

# Simülasyon döngüsü

1. Gazebo fizik durumunu **sensör verisine** çevirir
2. Veriyi SITL'e **gönderir**
3. SITL işler, **kontrol çıkışı** hesaplar
4. Motor komutlarını Gazebo'ya **geri gönderir**
5. Gazebo dünyayı **günceller**

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Hız</div>
  Bu döngü saniyede <strong>yüzlerce kez</strong> tekrarlanır.
</div>

---

<!-- ─────────── YENİ · SİM vs GERÇEK AKIŞ ─────────── -->

# Gerçek uçakta bu resim nasıl?

<div class="ky-ikili">

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Simülasyonda</div>
  Yer istasyonu → SITL → <strong>Gazebo</strong> → üretilmiş
  sensör verisi → SITL
</div>

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Gerçekte</div>
  Yer istasyonu → Pixhawk → <strong>motorlar</strong> → gerçek
  sensör verisi → Pixhawk
</div>

</div>

Değişen tek halka: fiziğin **nerede** hesaplandığı.

---

<!-- ─────────── 24 · 1.5 · PORT NEDİR ─────────── -->

# Port nedir?

<div class="ky-ikili">

<div>

Aynı bilgisayarda çalışan programların birbirine karışmadan
konuşmasını sağlayan **numara**.

- Her bağlantının bir portu var
- Bir portu **tek program** dinler
- Numaralar **rastgele değil**

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">En sık hata kaynağı</div>
  Yanlış port yazan program <strong>hata vermez</strong> — sessizce
  bekler. Bölüm 6'da buna geri döneceğiz.
</div>

</div>

---

<!-- ─────────── 25 · ÜÇ BAĞLANTI ─────────── -->

# Üç bağlantı, üç port

```mermaid {theme: 'base', scale: 1.05, themeVariables: {primaryColor: '#ffffff', primaryTextColor: '#14171c', primaryBorderColor: '#1257f0', lineColor: '#5a6473', edgeLabelBackground: '#f6f7f9', fontSize: '19px', fontFamily: 'Figtree'}}
flowchart LR
  A[Gazebo] -->|UDP 9002<br>FDM| B[SITL]
  B -->|TCP 5760<br>MAVProxy| C[Konsol]
  B -->|UDP 14550<br>MAVLink| D[Python / GCS]
  style A fill:#ffffff,stroke:#00a6a0,stroke-width:2px,color:#14171c
  style B fill:#ffffff,stroke:#1257f0,stroke-width:2px,color:#14171c
  style C fill:#ffffff,stroke:#dde1e8,stroke-width:2px,color:#5a6473
  style D fill:#ffffff,stroke:#6e4bf0,stroke-width:2px,color:#14171c
```

---

<!-- ─────────── 26 · PORT HARİTASI ─────────── -->

# Üç uçak, üç port grubu

```
Uçak    Instance   FDM     TCP     MAVLink
-----------------------------------------
1.      -I0        9002    5760    14550
2.      -I1        9012    5770    14560
3.      -I2        9022    5780    14570
```

Her yeni uçak için portlar **onar onar** artıyor.

---

<!-- ─────────── 27 · KURAL ─────────── -->

# Kural

```
port = taban + 10 × instance
```

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Bu kuralı ezberleme, mantığını tut</div>
  Kaç uçak açarsan aç, portu hesaplayabilirsin. Bölüm 3'te üç uçağı
  aynı anda kaldırırken bunu kullanacağız.
</div>

---

<!-- ─────────── YENİ · PORT ÇAKIŞMASI ─────────── -->

# Port çakışırsa ne olur?

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Belirti: sessizlik</div>
  Program çökmez — ekrana hiçbir şey yazmaz, öylece bekler.
</div>

- Aynı portu **iki program** dinleyemez
- İkincisi hata vermez, veri de alamaz
- **Kontrol:** `ss -lunp | grep 14550`
- Bölüm 6'da bununla karşılaşacağız

---

<!-- ─────────── 28 · ÖZET ─────────── -->

# Özet

- Uçuş kontrolcüsü = uçağın **beyni**, yazılımı **ArduPilot**
- **SITL** aynı beyni donanımsız çalıştırır
- **Gazebo** dünyayı, SITL beyni yürütür
- İçeride **FDM**, dışarıda **MAVLink**

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Sonraki bölüm</div>
  <strong>Bölüm 2 — Ortam kurulumu:</strong> bütün bu yığını kuracağız.
</div>
