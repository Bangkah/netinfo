# netinfo

![AUR version](https://img.shields.io/aur/version/netinfo?style=flat-square)
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

**netinfo** adalah utilitas command-line sederhana dan cepat untuk menampilkan informasi jaringan user secara detail. Cocok untuk troubleshooting, audit, scripting, atau sekadar mengetahui status koneksi Anda.

---


## Fitur Utama

- Menampilkan IP publik & lokal
- Deteksi ASN dan organisasi/ISP
- Reverse DNS lookup
- Estimasi tipe jaringan (Mobile/Fiber/DSL/Wireless/ISP)
- Info sistem: OS, kernel, arsitektur, hostname, terminal, shell
- Deteksi VPN/proxy (jika tersedia)

---

## Instalasi

### Melalui AUR (Arch User Repository)
```sh
yay -S netinfo
```


### Opsi

| Opsi           | Keterangan                      |
|----------------|----------------------------------|
| (tanpa opsi)   | Output lengkap (default)         |

### Contoh Penggunaan
- Output lengkap: `netinfo`

### Contoh Output
```
User Network Info
-----------------
Public IP    : 114.122.39.111
Local IP     : 192.168.8.191
IP Version   : IPv4
ASN          : AS23693
Organization : PT. Telekomunikasi Selular
Reverse DNS  : -
Network Type : ISP (estimated from ASN)

System Info
-----------
OS           : Linux
Kernel       : 6.18.6-zen1-1-zen
Architecture : x86_64
Hostname     : atha-ANV16-71-79NR
Terminal     : xterm-256color
Shell        : /usr/bin/zsh

Privacy
-------
VPN / Proxy  : No / Unknown
```
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

