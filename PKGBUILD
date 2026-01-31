# Maintainer: atha <your-email@example.com>

pkgname=netinfo
pkgver=1.0.0
pkgrel=1
pkgdesc="Command-line tool untuk melihat informasi jaringan user (IP, ISP, lokasi, ASN, dll)"
arch=('any')
url="https://github.com/atha/netinfo"
license=('MIT')
depends=('python' 'python-requests')
source=("netinfo.py")
sha256sums=('SKIP')

package() {
    install -Dm755 netinfo.py "$pkgdir/usr/bin/netinfo"
}
