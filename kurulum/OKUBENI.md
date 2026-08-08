# Kurulum dosyaları

Bölüm 2'de kullanılan, **kursa özel** dosyalar. Bunlar ArduPilot'un ya da
SITL_Models'in resmî depolarında **yoktur** — yalnızca burada.

| Dosya | Ne işe yarar | Hangi ders |
|---|---|---|
| `UAV_TRANSFER.tar.gz` | Üç UAV modeli (AV1, AV2, YEM), dünya dosyası, waypoint'ler | 2.17 |
| `create_satellite_ground.py` | Gazebo zeminine gerçek uydu görüntüsü koyar | 2.17 |

## Kullanım

**1 · UAV modelleri**

Dosyayı indir, ev dizinine koy:

```bash
mv ~/Downloads/UAV_TRANSFER.tar.gz ~/
cd ~ && tar -xzf UAV_TRANSFER.tar.gz
cd ~/UAV_TRANSFER && chmod +x install.sh && ./install.sh
```

**2 · Uydu görüntülü zemin** *(isteğe bağlı, internet gerekir)*

```bash
pip3 install --break-system-packages Pillow
mkdir -p ~/SITL_Models/Gazebo/scripts
cp create_satellite_ground.py ~/SITL_Models/Gazebo/scripts/
cd ~/SITL_Models/Gazebo/scripts
python3 create_satellite_ground.py
```

Script `~/SITL_Models/Gazebo/models/satellite_ground/` klasörünü üretir.
Koordinatlar dünya dosyasıyla eşleşecek şekilde sabittir
(`38.700853, 27.453821`); başka bir saha kullanacaksan script'in
başındaki `CENTER_LAT` / `CENTER_LON` değerlerini değiştir.

İnternetin yoksa bu adımı atla — Gazebo düz zeminle açılır, simülasyon
aynı şekilde çalışır.
