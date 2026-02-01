# netinfo

![AUR version](https://img.shields.io/aur/version/netinfo?style=flat-square)
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

**netinfo** adalah utilitas command-line sederhana dan cepat untuk menampilkan informasi jaringan user secara detail. Cocok untuk troubleshooting, audit, scripting, atau sekadar mengetahui status koneksi Anda.

---

## Fitur Utama

- Menampilkan IP publik & lokal
- Deteksi ISP, ASN, region, negara
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
| --short           | Output singkat (hanya IP publik & region)   |
| --public-only     | Hanya menampilkan IP publik                 |
| --anon            | Output anonim: hanya kota & negara, tanpa IP publik      |
| --safe-demo       | Output demo: IP publik diganti contoh, aman dibagikan    |

### Contoh Penggunaan
- Output lengkap: `netinfo`
- Output JSON: `netinfo --json`
- Output singkat: `netinfo --short`
- Hanya IP publik: `netinfo --public-only`
- Mode anonim: `netinfo --anon`
- Mode demo aman: `netinfo --safe-demo`

### Contoh Output Mode Demo Aman
```
User Network Info
-----------------
Public IP   : 103.xxx.xxx.xxx
Local IP    : 192.168.1.10
ISP         : Telkom Indonesia
ASN         : AS7713
Country     : ID
Continent   : Asia
Region      : Aceh
Accuracy    : Medium (IP-based estimation)
Timezone    : Asia/Jakarta
VPN/Proxy   : VPN: No/Unknown, Proxy: No/Unknown, Tor: No/Unknown (checked via IP)
OS          : Linux 6.18.6-zen1-1-zen
Terminal    : xterm-256color
User-Agent  : - (not available)
Ping        : 25.0 ms
```

### Contoh Output
```
User Network Info
-----------------
Public IP   : 114.122.39.111
Local IP    : 192.168.8.191
ISP         : PT. Telekomunikasi Selular
ASN         : AS23693
Country     : ID
Continent   : Asia
Region      : North Sumatra
Accuracy    : Medium (IP-based estimation)
Timezone    : Asia/Jakarta
VPN/Proxy   : VPN: No/Unknown, Proxy: No/Unknown, Tor: No/Unknown (checked via IP)
OS          : Linux 6.18.6-zen1-1-zen
Terminal    : xterm-256color
User-Agent  : - (not available)
Ping        : 56.26 ms
```

### Output JSON
```
netinfo --json
{
  "public_ip": "114.122.39.111",
  "local_ip": "192.168.8.191",
  "isp": "PT. Telekomunikasi Selular",
  "asn": "AS23693",
  "region": "North Sumatra",
  "country": "ID",
  "continent": "Asia",
  "geo_source": "ipinfo.io",
  "accuracy": "Medium (IP-based estimation)",
  "timezone": "Asia/Jakarta",
  "vpn_proxy": "VPN: No/Unknown, Proxy: No/Unknown, Tor: No/Unknown (checked via IP)",
  "os": "Linux 6.18.6-zen1-1-zen",
  "terminal_type": "xterm-256color",
  "user_agent": "- (not available)",
  "latency_ms": 56.26
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

