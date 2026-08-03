# Sürüm notları

Kurstaki komutlarla kendi sisteminde gördüğün çıktı farklıysa buraya bak.

| Tarih | Konu | Not |
|---|---|---|
| 2026-08 | `sim_vehicle.py` çıkış portları | Bu sürüm instance başına **tek** MAVLink çıkışı açıyor: `14550 + 10*instance`. Eski sürümlerde `14551` de açılıyordu; internetteki "14551 kullan" tavsiyeleri oradan kalma. Script için ayrı port istiyorsan `--out=udp:127.0.0.1:14551` ver. |

