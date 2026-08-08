#!/usr/bin/env python3
"""
Uydu Görüntülü Zemin Modeli Oluşturucu - Gazebo (gz sim) için
==============================================================
Bu script, belirtilen koordinatlar için uydu görüntüsü indirir
ve Gazebo'da kullanılabilir bir ground plane modeli oluşturur.

Kullanım:
    python3 create_satellite_ground.py

Gereksinimler:
    pip install Pillow

Çıktı:
    ~/SITL_Models/Gazebo/models/satellite_ground/ klasörüne model oluşturur
"""

import math
import urllib.request
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow kütüphanesi gerekli! Yükleniyor...")
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image

# ============================================================
# AYARLAR - İhtiyacına göre değiştir
# ============================================================
CENTER_LAT = 38.700853       # World dosyasındaki latitude
CENTER_LON = 27.453821       # World dosyasındaki longitude
WORLD_SIZE_M = 1000          # Kaplanacak alan (metre) - 1km x 1km
ZOOM = 18                    # Detay seviyesi (17-19 arası önerilir)
TILE_SIZE = 256              # Tile boyutu (değiştirme)

# Model çıktı klasörü
MODEL_DIR = os.path.expanduser("~/SITL_Models/Gazebo/models/satellite_ground")

# ============================================================
# FONKSİYONLAR
# ============================================================

def lat_lon_to_tile(lat, lon, zoom):
    """Lat/lon → tile x,y koordinatı"""
    n = 2 ** zoom
    x = int((lon + 180) / 360 * n)
    y = int((1 - math.log(math.tan(math.radians(lat)) + 1/math.cos(math.radians(lat))) / math.pi) / 2 * n)
    return x, y

def tile_to_lat_lon(x, y, zoom):
    """Tile x,y → lat/lon (NW köşe)"""
    n = 2 ** zoom
    lon = x / n * 360 - 180
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    return lat, lon

def meters_per_pixel(lat, zoom):
    """Belirtilen enlem ve zoom için piksel başına metre"""
    return 156543.03392 * math.cos(math.radians(lat)) / (2 ** zoom)

def download_tiles():
    """Uydu tile'larını indir ve birleştir"""
    
    mpp = meters_per_pixel(CENTER_LAT, ZOOM)
    pixels_needed = WORLD_SIZE_M / mpp
    tiles_needed = math.ceil(pixels_needed / TILE_SIZE) + 2
    
    center_tx, center_ty = lat_lon_to_tile(CENTER_LAT, CENTER_LON, ZOOM)
    half = tiles_needed // 2
    
    x_start = center_tx - half
    x_end = center_tx + half
    y_start = center_ty - half
    y_end = center_ty + half
    
    cols = x_end - x_start + 1
    rows = y_end - y_start + 1
    total = cols * rows
    
    print(f"📍 Koordinat: {CENTER_LAT}, {CENTER_LON}")
    print(f"📐 Alan: {WORLD_SIZE_M}m x {WORLD_SIZE_M}m")
    print(f"🔍 Zoom: {ZOOM} (piksel başına {mpp:.3f}m)")
    print(f"📦 İndirilecek tile: {total} ({cols}x{rows})")
    print()
    
    # Tile'ları indir
    tile_dir = os.path.join(MODEL_DIR, "_tiles_cache")
    os.makedirs(tile_dir, exist_ok=True)
    
    downloaded = 0
    cached = 0
    failed = 0
    
    # ESRI World Imagery - ücretsiz uydu görüntüsü servisi
    base_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    
    for ty in range(y_start, y_end + 1):
        for tx in range(x_start, x_end + 1):
            fname = os.path.join(tile_dir, f"{tx}_{ty}.png")
            if os.path.exists(fname):
                cached += 1
                continue
            
            url = base_url.format(z=ZOOM, y=ty, x=tx)
            try:
                urllib.request.urlretrieve(url, fname)
                downloaded += 1
                progress = downloaded + cached + failed
                print(f"\r⬇️  İndiriliyor... {progress}/{total}", end="", flush=True)
            except Exception as e:
                failed += 1
                print(f"\n⚠️  Tile başarısız ({tx},{ty}): {e}")
    
    print(f"\n✅ İndirilen: {downloaded}, Önbellekten: {cached}, Başarısız: {failed}")
    
    if downloaded + cached == 0:
        print("\n❌ Hiç tile indirilemedi! İnternet bağlantınızı kontrol edin.")
        print("   Alternatif olarak Google Maps'ten ekran görüntüsü alabilirsiniz.")
        sys.exit(1)
    
    # Tile'ları birleştir
    print("\n🧩 Tile'lar birleştiriliyor...")
    stitched = Image.new('RGB', (cols * TILE_SIZE, rows * TILE_SIZE))
    
    for ty in range(y_start, y_end + 1):
        for tx in range(x_start, x_end + 1):
            fname = os.path.join(tile_dir, f"{tx}_{ty}.png")
            if os.path.exists(fname):
                try:
                    tile = Image.open(fname)
                    px = (tx - x_start) * TILE_SIZE
                    py = (ty - y_start) * TILE_SIZE
                    stitched.paste(tile, (px, py))
                except:
                    pass
    
    # Boyutları hesapla
    nw_lat, nw_lon = tile_to_lat_lon(x_start, y_start, ZOOM)
    se_lat, se_lon = tile_to_lat_lon(x_end + 1, y_end + 1, ZOOM)
    
    center_lat_rad = math.radians(CENTER_LAT)
    actual_width_m = (se_lon - nw_lon) * math.cos(center_lat_rad) * 111320
    actual_height_m = (nw_lat - se_lat) * 110540
    
    # Merkez offset
    img_center_lat = (nw_lat + se_lat) / 2
    img_center_lon = (nw_lon + se_lon) / 2
    offset_x = (img_center_lon - CENTER_LON) * math.cos(center_lat_rad) * 111320
    offset_y = (img_center_lat - CENTER_LAT) * 110540
    
    # Görüntüyü kaydet
    tex_dir = os.path.join(MODEL_DIR, "materials", "textures")
    os.makedirs(tex_dir, exist_ok=True)
    
    img_path = os.path.join(tex_dir, "satellite.png")
    
    # Boyutu optimize et (max 4096x4096)
    max_size = 4096
    if stitched.width > max_size or stitched.height > max_size:
        stitched = stitched.resize((max_size, max_size), Image.LANCZOS)
        print(f"📏 Görüntü {max_size}x{max_size} boyutuna küçültüldü")
    
    stitched.save(img_path, "PNG", optimize=True)
    print(f"💾 Uydu görüntüsü kaydedildi: {img_path}")
    print(f"📐 Kaplanan alan: {actual_width_m:.1f}m x {actual_height_m:.1f}m")
    
    return actual_width_m, actual_height_m, offset_x, offset_y

def create_model_sdf(width, height, offset_x, offset_y):
    """Gazebo SDF model dosyasını oluştur"""
    
    sdf_content = f"""<?xml version="1.0" ?>
<sdf version="1.7">
  <model name="satellite_ground">
    <static>true</static>
    <link name="link">
      <collision name="collision">
        <geometry>
          <plane>
            <normal>0 0 1</normal>
            <size>{width:.1f} {height:.1f}</size>
          </plane>
        </geometry>
      </collision>
      <visual name="visual">
        <geometry>
          <plane>
            <normal>0 0 1</normal>
            <size>{width:.1f} {height:.1f}</size>
          </plane>
        </geometry>
        <material>
          <diffuse>1.0 1.0 1.0 1</diffuse>
          <specular>0.0 0.0 0.0 1</specular>
          <pbr>
            <metal>
              <albedo_map>materials/textures/satellite.png</albedo_map>
              <roughness>1.0</roughness>
              <metalness>0.0</metalness>
            </metal>
          </pbr>
        </material>
      </visual>
    </link>
  </model>
</sdf>
"""
    
    sdf_path = os.path.join(MODEL_DIR, "model.sdf")
    with open(sdf_path, "w") as f:
        f.write(sdf_content)
    print(f"📄 Model SDF kaydedildi: {sdf_path}")
    
    # model.config dosyası
    config_content = """<?xml version="1.0" ?>
<model>
  <name>satellite_ground</name>
  <version>1.0</version>
  <sdf version="1.7">model.sdf</sdf>
  <description>
    Uydu görüntülü zemin modeli.
    Koordinat: {lat}, {lon}
  </description>
</model>
""".format(lat=CENTER_LAT, lon=CENTER_LON)
    
    config_path = os.path.join(MODEL_DIR, "model.config")
    with open(config_path, "w") as f:
        f.write(config_content)
    print(f"📄 Model config kaydedildi: {config_path}")
    
    return offset_x, offset_y

def print_world_snippet(offset_x, offset_y):
    """World dosyasına eklenecek kodu göster"""
    
    print("\n" + "="*60)
    print("✅ MODEL BAŞARIYLA OLUŞTURULDU!")
    print("="*60)
    print()
    print("World dosyandaki ground_plane modelini şununla değiştir:")
    print("-"*60)
    print(f"""
    <!-- Uydu Görüntülü Zemin -->
    <include>
      <uri>model://satellite_ground</uri>
      <pose>{offset_x:.2f} {offset_y:.2f} -0.01 0 0 0</pose>
    </include>
""")
    print("-"*60)
    print()
    print("Gazebo'yu başlatırken resource path'e modeli eklemeyi unutma:")
    print("  export GZ_SIM_RESOURCE_PATH=$HOME/SITL_Models/Gazebo/models:$HOME/SITL_Models/Gazebo/worlds")
    print()

# ============================================================
# ANA PROGRAM
# ============================================================
if __name__ == "__main__":
    print("🛰️  Uydu Görüntülü Zemin Modeli Oluşturucu")
    print("=" * 50)
    print()
    
    width, height, offset_x, offset_y = download_tiles()
    create_model_sdf(width, height, offset_x, offset_y)
    print_world_snippet(offset_x, offset_y)
