---
theme: default
title: Bölüm 3 — İlk Uçuş
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
     BÖLÜM 3 — İLK UÇUŞ · 6 ders · 14 slayt · ~56 dakika

     3.1  sim_vehicle.py anatomisi   slayt 3-4    10 dk
     3.2  MAVProxy ekranı            slayt 5-6     8 dk
     3.3  İlk kalkış                 slayt 7-8    10 dk
     3.4  Gazebo + SITL birlikte     slayt 9-10   10 dk
     3.5  Üç uçak aynı anda          slayt 11-12  10 dk
     3.6  Başlatma script'i          slayt 13      8 dk

     DEMO ağırlıklı bölüm: slaytlar noktalama, iş terminalde ve
     Gazebo'da. Komutların tamamı çekim metninde.

     KAYNAKTAN DOĞRULANDI (3 Ağustos 2026):
       models/mini_talon_vtail/model.sdf         fdm_port_in 9002
       models/mini_talon_vtail_target/model.sdf  fdm_port_in 9012
       models/mini_talon_vtail_third/model.sdf   fdm_port_in 9022
       worlds/dual_vtail_runway_3uav.sdf         üç modeli de içeriyor
       config/mini_talon_vtail.param             mevcut
     ═══════════════════════════════════════════════════════════ -->

<!-- ─────────── 1 · KAPAK ─────────── -->

<div class="ky-kapak-serit"></div>

# İlk Uçuş

<div class="ky-kapak-alt">

Bölüm 3 · Tek uçaktan üç uçağa

</div>

---

<!-- ─────────── 2 · BU BÖLÜMDE ─────────── -->

# Bu bölümde

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      Tek uçağı <strong>havalandıracağız</strong> — Gazebo'suz
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      Gazebo ile <strong>birleştireceğiz</strong> — görsel uçuş
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Üç uçağı</strong> aynı anda kaldıracağız
    </div>
  </div>

</div>

---

<!-- ─────────── 3 · 3.1 · KOMUT ─────────── -->

# `sim_vehicle.py` anatomisi

```
sim_vehicle.py -v ArduPlane --console --map
```

- `-v ArduPlane` → hangi **araç tipi**
- `--console` → telemetri penceresi
- `--map` → harita penceresi

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Tek başına çalışır</div>
  Gazebo gerekmez; ArduPilot kendi basit fiziğini kullanır.
</div>

---

<!-- ─────────── 4 · GAZEBO'LU HALİ ─────────── -->

# Gazebo'ya bağlanan hali

```
sim_vehicle.py -v ArduPlane -f JSON --model JSON \
  --add-param-file=.../mini_talon_vtail.param \
  --console --map -I0
```

- `-f JSON --model JSON` → fiziği **dışarıdan** al
- `--add-param-file` → uçağa özel ayarlar
- `-I0` → **instance** numarası

Fark tek cümlede: fiziği artık **Gazebo** hesaplıyor.

---

<!-- ─────────── 5 · 3.2 · ÜÇ PENCERE ─────────── -->

# Ekranda üç pencere

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mor">
    <div class="ky-kart__ust">⌨</div>
    <div class="ky-kart__govde">
      <strong>Terminal</strong><br>
      MAVProxy komut satırı — komutları buraya yazıyoruz
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">▤</div>
    <div class="ky-kart__govde">
      <strong>Konsol</strong><br>
      İrtifa, hız, batarya, uçuş modu
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">◉</div>
    <div class="ky-kart__govde">
      <strong>Harita</strong><br>
      Uçağın konumu ve rotası
    </div>
  </div>

</div>

---

<!-- ─────────── 6 · MAVPROXY KOMUTLARI ─────────── -->

# Bilmen gereken komutlar

```
mode GUIDED     tek hedefe otonom uçuş
mode AUTO       waypoint takibi
mode RTL        eve dön
arm throttle    motoru aç
disarm          motoru kapat
takeoff 50      50 metreye kalk
```

Bu bölümde ilk dördünü kullanacağız.

---

<!-- ─────────── 7 · 3.3 · KALKIŞ DİZİSİ ─────────── -->

# Kalkış dizisi

```
param set ARMING_CHECK 0
mode GUIDED
arm throttle
takeoff 50
```

Sıra **değiştirilemez**: mod önce, arm sonra, kalkış en son.

---

<!-- ─────────── 8 · TUZAK: ARMING_CHECK ─────────── -->

# Neden `ARMING_CHECK 0`?

<div class="ky-ikili">

<div>

ArduPilot arm etmeden önce onlarca kontrol yapıyor:
GPS kilidi, pusula, batarya, RC sinyali.

Simülasyonda bunların bir kısmı **hiç yok**.

</div>

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Gerçek uçakta ASLA</div>
  Bu ayar yalnızca simülasyon içindir. Gerçek uçakta kapatmak,
  emniyet kemerini kesmek gibidir.
</div>

</div>

---

<!-- ─────────── 9 · 3.4 · DÖRT TERMİNAL ─────────── -->

# Gazebo + SITL: dört terminal

- **1 ·** Gazebo — dünyayı açar
- **2 ·** SITL `-I0` — birinci uçak
- **3 ·** SITL `-I1` — ikinci uçak
- **4 ·** SITL `-I2` — üçüncü uçak

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Sıra önemli</div>
  Önce Gazebo açılır ve dünya <strong>tam yüklenir</strong>, sonra
  uçaklar bağlanır.
</div>

---

<!-- ─────────── 10 · TUZAK: PLAY ─────────── -->

# Tuzak — uçak bağlanmıyor

<div class="ky-kutu ky-kutu--uyari">
  <div class="ky-kutu__baslik">Waiting for heartbeat…</div>
  SITL bağlanamıyor, terminal öylece bekliyor.
</div>

- **Sebep 1:** Simülasyon **duraklatılmış** — `-r` yoksa oynat'a bas
- **Sebep 2:** Dünya yüklenmeden SITL başlatılmış
- **Çözüm:** dünyanın açılmasını bekle, sonra SITL'i başlat

---

<!-- ─────────── 11 · 3.5 · ÜÇ UÇAK ─────────── -->

# Üç uçak, üç instance

```
Instance   Model dizini              FDM
--------------------------------------------
-I0        mini_talon_vtail          9002
-I1        mini_talon_vtail_target   9012
-I2        mini_talon_vtail_third    9022
```

Her instance, dünyadaki **ayrı bir modele** bağlanıyor.

---

<!-- ─────────── 12 · HANGİSİ HANGİSİ ─────────── -->

# Hangi uçak hangisi?

<div class="ky-kartlar">

  <div class="ky-kart ky-kart--mavi">
    <div class="ky-kart__ust">1</div>
    <div class="ky-kart__govde">
      <strong>Mavi</strong> · <code>-I0</code><br>
      Ana uçağımız — Bölüm 6'da bunu kodlayacağız
    </div>
  </div>

  <div class="ky-kart ky-kart--pembe">
    <div class="ky-kart__ust">2</div>
    <div class="ky-kart__govde">
      <strong>Kırmızı</strong> · <code>-I1</code><br>
      Hedef uçak — takip senaryolarında
    </div>
  </div>

  <div class="ky-kart ky-kart--turkuaz">
    <div class="ky-kart__ust">3</div>
    <div class="ky-kart__govde">
      <strong>Yeşil</strong> · <code>-I2</code><br>
      Kameralı uçak — Bölüm 7'de kullanacağız
    </div>
  </div>

</div>

---

<!-- ─────────── 13 · 3.6 · SCRIPT ─────────── -->

# Dört terminali tek komuta indirmek

<div class="ky-ikili">

<div>

Her seferinde dört pencere açmak yorucu. Bir script yazıp
otomatikleştiriyoruz.

- Gazebo'yu açar
- 8 saniye **bekler**
- Üç uçağı sırayla başlatır

</div>

<div class="ky-kutu">
  <div class="ky-kutu__baslik">Neden bekleme var?</div>
  Dünya yüklenmeden bağlanan SITL, heartbeat bulamaz. O
  <code>sleep</code> satırı bu yüzden orada.
</div>

</div>

---

<!-- ─────────── 14 · ÖZET ─────────── -->

# Özet

- `sim_vehicle.py` tek başına da, Gazebo ile de çalışır
- Kalkış: **mod → arm → takeoff**
- Gazebo'da **oynat** tuşu unutulmaz
- Her uçak kendi **instance** ve **portunu** kullanır

<div class="ky-kutu ky-kutu--olumlu">
  <div class="ky-kutu__baslik">Sonraki bölüm</div>
  <strong>Bölüm 4 — Görev planlama:</strong> rota çizip AUTO'da uçuş.
</div>
