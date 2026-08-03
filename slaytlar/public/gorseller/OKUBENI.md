# Görseller

Slaytlarda kullanacağın resimler buraya. Slidev `public/` altındakileri
kök yoldan sunar, yani buraya koyduğun `heartbeat.png` slaytta
`/gorseller/heartbeat.png` olur — `public` yazmıyorsun.

## Kullanım

**Metin + yan görsel** (bolum-03.md, 3. slayt):

```html
<div class="ky-ikili">
  <div>

  Buraya metin, madde listesi vs.

  </div>

  <figure class="ky-gorsel">
    <img src="/gorseller/heartbeat.png" alt="Ne olduğunu anlatan kısa metin">
    <figcaption>Altyazı — isteğe bağlı</figcaption>
  </figure>
</div>
```

Görseli sola almak için `<div class="ky-ikili ky-ikili--ters">`.

**Tam ekran görsel** (8. slayt):

```html
<div class="ky-tam-gorsel">
  <img src="/gorseller/saha.jpg" alt="...">
</div>
<div class="ky-tam-yazi">

# Başlık

Üstteki koyu perde yazının okunmasını sağlıyor.

</div>
```

## Boyut önerileri

| Nerede | En az çözünürlük | Not |
|---|---|---|
| Yan görsel (`ky-ikili`) | 960 × 720 | slaytın yarısını kaplar |
| Tam ekran | 1920 × 1080 | daha küçüğü kayıtta bulanıklaşır |

Ekran görüntüsü alıyorsan **1080p'den küçük alma** — slayt 1920×1080'e
ölçekleniyor, altındaki her şey videoda yumuşuyor.

## Filigran / logo

Kendi logonu her slaydın arkasına soluk filigran olarak koymak istersen:
`logo.svg` adıyla buraya bırak, sonra `tema/stil.css` içindeki

```css
--ky-filigran: none;
```

satırını

```css
--ky-filigran: url('/gorseller/logo.svg');
```

yap. Opaklık %5'e sabitli, metnin önüne geçmez.
