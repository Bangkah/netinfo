# netinfo

Command-line tool untuk melihat informasi jaringan user (IP publik, lokal, ISP, lokasi, ASN, VPN/proxy, User-Agent).

## Instalasi (Arch Linux)

1. Pastikan `python` dan `python-requests` sudah terpasang.
2. Clone repo ini atau download source.
3. Jalankan:

    makepkg -si

4. Jalankan tool dengan perintah:

    netinfo

## Opsi Penggunaan

- `netinfo` : Output lengkap (default)
- `netinfo --json` : Output dalam format JSON
- `netinfo --short` : Output singkat (hanya IP publik & kota)
- `netinfo --public-only` : Hanya menampilkan IP publik

## Output Contoh

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

## Lisensi
MIT
