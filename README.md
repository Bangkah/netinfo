# netinfo

netinfo adalah tool command-line untuk menampilkan informasi jaringan user secara cepat dan praktis. Data yang ditampilkan meliputi IP publik, IP lokal, ISP, lokasi (kota/region/negara), ASN, status VPN/proxy, timezone, dan User-Agent.

## Instalasi

### Melalui AUR (Arch User Repository)
jalankan:

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
User Info
---------
Public IP   : 103.xxx.xxx.xxx
Local IP    : 192.168.1.10
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
## Kontribusi

Pull request, issue, dan saran sangat dipersilakan! Pastikan perubahan Anda jelas dan teruji.

## Lisensi

MIT. Lihat file LICENSE untuk detail.

---

![AUR version](https://img.shields.io/aur/version/netinfo?style=flat-square)
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

**netinfo** adalah utilitas command-line sederhana dan cepat untuk menampilkan informasi jaringan user secara detail. Cocok untuk troubleshooting, audit, atau sekadar mengetahui status koneksi Anda.

---

## Fitur Utama

- Menampilkan IP publik & lokal
- Deteksi ISP, ASN, lokasi (kota, region, negara)
- Deteksi timezone
- Status VPN/proxy (jika tersedia)
- Output JSON untuk scripting/otomasi
- Output singkat (hanya IP & kota)

---

## Instalasi

### Melalui AUR (Arch User Repository)
```sh
yay -S netinfo
```

### Manual (build lokal)
```sh
git clone https://github.com/Bangkah/netinfo.git
cd netinfo
makepkg -si
```

---

## Penggunaan

```sh
netinfo [opsi]
```

### Opsi

| Opsi              | Keterangan                                 |
|-------------------|---------------------------------------------|
| (tanpa opsi)      | Output lengkap (default)                    |
| --json            | Output dalam format JSON                    |
| --short           | Output singkat (hanya IP publik & kota)     |
| --public-only     | Hanya menampilkan IP publik                 |

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

---

**Maintainer:**

- Bangkah <your-email@example.com>

---

Sumber: [AUR netinfo](https://aur.archlinux.org/packages/netinfo) | [GitHub](https://github.com/Bangkah/netinfo)

