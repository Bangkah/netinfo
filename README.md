# netinfo

![AUR version](https://img.shields.io/aur/version/netinfo?style=flat-square)
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

**netinfo** adalah utilitas command-line sederhana dan cepat untuk menampilkan informasi jaringan user secara detail. Cocok untuk troubleshooting, audit, scripting, atau sekadar mengetahui status koneksi Anda.

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

## Kontribusi

Pull request, issue, dan saran sangat dipersilakan! Pastikan perubahan Anda jelas dan teruji. Lihat PKGBUILD dan LICENSE untuk detail.

## Lisensi

MIT. Lihat file LICENSE untuk detail.

---

**Maintainer:**

- Bangkah mdhyaulatha@gmail.com

---

Sumber: [AUR netinfo](https://aur.archlinux.org/packages/netinfo) | [GitHub](https://github.com/Bangkah/netinfo)

