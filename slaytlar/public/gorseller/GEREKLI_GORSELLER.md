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

## Bölüm 0 — Kursa Giriş · ✅ TAMAM

Yer tutucu kalmadı, dört görselin dördü de yerinde.

| Dosya | Slayt | Kaynak | Not |
|---|---|---|---|
| `b0-final-demo.jpg` | 3 (tam ekran) | `gazebo_uc_ucak.png` | Arayüz panelleri kırpıldı, 16:9. **Uçaklar pistte, havada değil** — havadayken çekilmiş daha yakın bir kare bu slaydı belirgin şekilde güçlendirir |
| `b0-ubuntu-masaustu.jpg` | 7 | `ubuntu_22.04.jpeg` | 656×467, önerilenin altında ama çerçevede 1.09× büyütüldüğü için sorun çıkarmıyor |
| `b0-github-depo.jpg` | 10 | `github_repo.png` | Tarayıcı çubuğu ve About paneli kırpıldı |
| `b0-rehber-pdf.jpg` | 11 | rehber PDF s.19 | **GEÇİCİ** — kursun kendi yazılı rehberi hazırlanınca değişecek |

**Zaten vardı:** `sitl_images.jpeg` (slayt 5), `pixhawk.jpg` (slayt 8).

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
