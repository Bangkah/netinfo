# netinfo

netinfo adalah tool command-line untuk menampilkan informasi jaringan user secara cepat dan praktis. Data yang ditampilkan meliputi IP publik, IP lokal, ISP, lokasi (kota/region/negara), ASN, status VPN/proxy, timezone, dan User-Agent.

## Instalasi

### Melalui AUR (Arch User Repository)
Jika sudah dipublish ke AUR, cukup jalankan:

    yay -S netinfo

### Manual (build lokal)
1. Pastikan `python` dan `python-requests` sudah terpasang.
2. Clone repo ini atau download source.
3. Build dan install dengan:

    makepkg -si

## Penggunaan

Jalankan perintah berikut di terminal:

    netinfo

### Opsi
- `netinfo` : Output lengkap (default)
- `netinfo --json` : Output dalam format JSON
- `netinfo --short` : Output singkat (hanya IP publik & kota)
- `netinfo --public-only` : Hanya menampilkan IP publik

### Contoh Output
```
User Info
---------
Public IP   : 103.xxx.xxx.xxx
Local IP    : 192.168.1.10
ISP         : Telkom Indonesia
Location    : Banda Aceh, Indonesia
Timezone    : Asia/Jakarta
ASN         : AS7713
VPN/Proxy   : No/Unknown
User-Agent  : - (not available)
```

### Output JSON
```
netinfo --json
{
  "public_ip": "103.xxx.xxx.xxx",
  "local_ip": "192.168.1.10",
  "isp": "Telkom Indonesia",
  "location": "Banda Aceh, Indonesia",
  "city": "Banda Aceh",
  "region": "Aceh",
  "country": "ID",
  "timezone": "Asia/Jakarta",
  "asn": "AS7713",
  "vpn_proxy": "No/Unknown",
  "user_agent": "- (not available)"
}
```

## Kontribusi & Lisensi
Kontribusi dipersilakan! Lihat PKGBUILD dan LICENSE untuk detail.
Lisensi: MIT
