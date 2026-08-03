# Gerekli görseller — bölüm bölüm

Slaytlarda **kesikli çerçeveli kutu** gördüğün her yer, henüz gelmemiş bir
görselin yeri. Kutunun içinde beklenen dosya adı yazıyor.

**Nasıl eklenir:** görseli bu klasöre (`public/gorseller/`) o adla koy, sonra
slayttaki `<div class="ky-gorsel-yer">…</div>` bloğunu şununla değiştir:

```html
<figure class="ky-gorsel">
  <div class="ky-gorsel__cerceve">
    <img src="/gorseller/DOSYA-ADI" alt="kısa açıklama">
  </div>
  <figcaption>Altyazı</figcaption>
</figure>
```

Bana linki gönderirsen indirip yerine yerleştiririm.

**Çözünürlük kuralı:** yan görsel en az **960×720**, tam ekran en az
**1920×1080**. Altındaki her şey 1080p kayıtta yumuşuyor.

---

## Bölüm 0 — Kursa Giriş

| Dosya adı | Slayt | Ne olmalı | Boyut |
|---|---|---|---|
| `b0-final-demo.jpg` | 3 (tam ekran) | Gazebo'da 3 uçak havada, uydu haritalı zemin. **Kursun vitrini** — en iyi kareyi buraya koy | 1920×1080 |
| `b0-ubuntu-masaustu.png` | 7 | Ubuntu 22.04 masaüstü, bir terminal açık | 960×720 |
| `b0-github-depo.png` | 10 | Kurs GitHub deposunun ana sayfası | 960×720 |
| `b0-rehber-pdf.png` | 11 | PDF rehberin kapağı veya bir kurulum sayfası | 960×720 |

**Hazır olanlar:** `sitl_images.jpeg` (slayt 5), `pixhawk.jpg` (slayt 8).

---

## Bölüm 1 — Temel Kavramlar *(sıradaki)*

| Dosya adı | Ders | Ne olmalı | Boyut |
|---|---|---|---|
| `b1-sabit-kanat.jpg` | 1.1 | Sabit kanat İHA, tercihen kendi uçağınız | 960×720 |
| `b1-multirotor.jpg` | 1.1 | Multirotor/quadcopter | 960×720 |
| `b1-pixhawk-yakin.jpg` | 1.2 | Uçuş kartının yakın çekimi, portları görünsün | 960×720 |
| `b1-ardupilot-logo.png` | 1.2 | ArduPilot logosu (şeffaf zemin) | — |
| `b1-px4-logo.png` | 1.2 | PX4 logosu (şeffaf zemin) | — |
| `b1-gazebo-dunya.jpg` | 1.3 | Gazebo'da uçak, uydu haritalı zemin | 960×720 |

**Zaten elimizde (rehberden çıkarıldı):** `rehber/` klasöründe

| Dosya | Rehberdeki adı | Kullanılacağı ders |
|---|---|---|
| `rehber/resim3-mimari-3katman.jpg` | Resim 3 | 1.4 |
| `rehber/resim4-port-diyagrami.jpg` | Resim 4 | 1.5 |
| `rehber/resim5-simulasyon-akisi.jpg` | Resim 5 | 1.4 |
| `rehber/resim6-sim-vs-gercek.jpg` | Resim 6 | 1.3 |
| `rehber/resim1-mavproxy-waypoint.jpg` | Resim 1 | 4.4 |
| `rehber/resim2-mission-planner-udp.jpg` | Resim 2 | 4.5 |
| `rehber/resim7-final-senaryo.jpg` | Resim 7 | 8.1 |

> **Uyarı:** rehberden çıkan diyagramların çözünürlüğü düşük (663×718 –
> 957×511). PDF'te iyi görünüyorlar ama 1080p videoda yumuşayacaklar.
> Resim 3, 4 ve 5 **mermaid ile yeniden çizilecek** — hem keskin olur hem
> port numaraları bizim kurulumumuza (5760/9002, 5770/9012, 5780/9022)
> uyar. Resim 4'teki FlightGear ve APM Planner kutuları bizde yok zaten.
> Resim 1, 2 ve 7 ekran görüntüsü/şema olduğu için olduğu gibi kullanılabilir,
> ama Resim 1 ve 2'yi kendi ekranından yeniden alman daha temiz olur.
