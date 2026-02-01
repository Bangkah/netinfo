#!/usr/bin/env python3
import socket
import requests
import json
import os
import argparse
import re

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "-"

def get_public_info():
    try:
        resp = requests.get("https://ipinfo.io/json", timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}

def get_user_agent():
    return os.environ.get("HTTP_USER_AGENT", "- (not available)")

def get_ipapi_info(ip=None):
    url = f"http://ip-api.com/json/{ip or ''}?fields=status,message,country,regionName,city,lat,lon,query,as,timezone"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}

def main():
    local_ip = get_local_ip()
    info = get_public_info()
    public_ip = info.get("ip", "-")
    isp = info.get("org", "-")
    asn = "-"
    if isp != "-":
        asn = isp.split()[0] if isp.startswith("AS") else "-"
    org = info.get("org", "-")
    city = info.get("city", "-")
    region = info.get("region", "-")
    country = info.get("country", "-")
    timezone = info.get("timezone", "-")
    user_agent = get_user_agent()
    vpn_proxy = info.get("privacy", {}).get("vpn", False) or info.get("privacy", {}).get("proxy", False)
    vpn_status = "Yes" if vpn_proxy else "No/Unknown"

    geo_source1 = "ipinfo.io"
    ipapi = get_ipapi_info(public_ip)
    geo_source2 = "ip-api.com"
    if not city or not region or not country:
        if ipapi.get("city"): city = ipapi["city"]
        if ipapi.get("regionName"): region = ipapi["regionName"]
        if ipapi.get("country"): country = ipapi["country"]
        if ipapi.get("as"): asn = ipapi["as"]
        if ipapi.get("timezone"): timezone = ipapi["timezone"]

    import time
    # Ambil latitude, longitude dari ip-api jika tersedia
    latitude = ipapi.get("lat") if ipapi.get("lat") is not None else info.get("loc", "").split(",")[0] if info.get("loc") else None
    longitude = ipapi.get("lon") if ipapi.get("lon") is not None else info.get("loc", "").split(",")[1] if info.get("loc") else None
    # Map URL
    map_url = None
    if latitude and longitude:
        try:
            lat_str = str(float(latitude))
            lon_str = str(float(longitude))
            map_url = f"https://www.google.com/maps?q={lat_str},{lon_str}"
        except Exception:
            map_url = None
    # ISP Name
    isp_name = None
    if org and org.startswith("AS"):
        isp_name = org.split(" ", 1)[1] if len(org.split(" ", 1)) > 1 else org
    else:
        isp_name = org
    # Continent (simple mapping)
    continent_map = {
        "ID": "Asia", "SG": "Asia", "MY": "Asia", "US": "North America", "GB": "Europe", "DE": "Europe", "FR": "Europe", "JP": "Asia", "CN": "Asia", "RU": "Europe/Asia", "BR": "South America", "AU": "Oceania"
    }
    continent = continent_map.get(country, "Unknown")
    # VPN/Proxy/Tor detection
    tor_status = "No/Unknown"
    if info.get("privacy", {}).get("tor", False):
        tor_status = "Yes (Tor exit node)"
    proxy_status = "Yes" if info.get("privacy", {}).get("proxy", False) else "No/Unknown"
    vpn_status = "Yes" if info.get("privacy", {}).get("vpn", False) else "No/Unknown"
    vpn_proxy_detail = f"VPN: {vpn_status}, Proxy: {proxy_status}, Tor: {tor_status} (checked via IP)"
    # Ping/latency check
    def ping(host):
        import subprocess
        try:
            start = time.time()
            out = subprocess.run(["ping", "-c", "1", "-W", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            end = time.time()
            if out.returncode == 0:
                # Parse ms from output
                for line in out.stdout.decode().splitlines():
                    if "time=" in line:
                        ms = line.split("time=")[1].split(" ")[0]
                        return float(ms)
                return round((end-start)*1000, 2)
            else:
                return None
        except Exception:
            return None
    latency = ping("8.8.8.8")
    import platform
    # Deteksi OS
    os_info = platform.system() + " " + platform.release()
    # Deteksi terminal type
    term_type = os.environ.get("TERM", "-")
    # Deteksi browser/user-agent jika dijalankan di client
    browser_info = os.environ.get("HTTP_USER_AGENT", None)
    if browser_info:
        user_agent_info = browser_info
    else:
        user_agent_info = get_user_agent()

    parser = argparse.ArgumentParser(description="Tampilkan info jaringan user.")
    parser.add_argument('--json', action='store_true', help='Output dalam format JSON')
    parser.add_argument('--short', action='store_true', help='Output singkat: IP publik & kota')
    parser.add_argument('--public-only', action='store_true', help='Hanya tampilkan IP publik')
    parser.add_argument('--anon', action='store_true', help='Output anonim: hanya kota & negara, tanpa IP')
    parser.add_argument('--safe-demo', action='store_true', help='Output demo: IP publik diganti contoh, aman dibagikan')
    parser.add_argument('-v', '--version', action='store_true', help='Tampilkan versi netinfo')
    parser.add_argument('--geo-debug', action='store_true', help='Tampilkan data mentah GeoIP dari semua API')
    args = parser.parse_args()

    def parse_latlong(loc):
        if loc and re.match(r"^-?\d+\.\d+,-?\d+\.\d+$", loc):
            lat, lon = loc.split(',')
            return float(lat), float(lon)
        return None, None

    def accuracy_label(asn):
        if asn and ("Telkomsel" in asn or "Indosat" in asn or "XL" in asn or "Tri" in asn):
            return "Low (Mobile ISP, routing)"
        return "Medium (IP-based estimation)"

    # ...existing code...
    city_out = city

    data = {
        "public_ip": public_ip,
        "local_ip": local_ip,
        "isp": isp_name,
        "asn": asn,
        "region": region,
        "country": country,
        "continent": continent,
        "geo_source": geo_source1,
        "accuracy": accuracy_label(asn),
        "timezone": timezone,
        "vpn_proxy": vpn_proxy_detail,
        "os": os_info,
        "terminal_type": term_type,
        "user_agent": user_agent_info,
        "latency_ms": latency
    }


    if args.version:
        print("netinfo 1.1.0 (cli) (built: Feb 1 2026)")
        print("Copyright (c) Bangkah, 2024-2026")
        print("Netinfo Engine v1.1.0, Copyright (c) Bangkah Technologies")
        return
    if args.anon:
        print(f"Kota: {city}\nNegara: {country}")
        return
    elif args.safe_demo:
        demo_ip = "103.xxx.xxx.xxx"
        print("User Info\n---------")
        print(f"Public IP   : {demo_ip}")
        print(f"Local IP    : {local_ip}")
        print(f"ISP         : {org}")
        print(f"Location    : {city_out}, {region}, {country}")
        print(f"Timezone    : {timezone}")
        print(f"ASN         : {asn}")
        print(f"VPN/Proxy   : {vpn_status}")
        print(f"User-Agent  : {user_agent}")
        return
    elif args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    elif args.short:
        print(f"Public IP : {public_ip}\nLocal IP  : {local_ip}\nKota      : {city}")
        return
    elif args.public_only:
        print(f"Public IP : {public_ip}\nLocal IP  : {local_ip}")
        return

    # Output default lengkap (valid, profesional, polished)
    print("User Network Info\n-----------------")
    print(f"Public IP   : {public_ip}")
    print(f"Local IP    : {local_ip}")
    print(f"ISP         : {isp_name}")
    print(f"ASN         : {asn}")
    print(f"Country     : {country}")
    print(f"Continent   : {continent}")
    print(f"Region      : {region}")
    print(f"Accuracy    : {accuracy_label(asn)}")
    print(f"Timezone    : {timezone}")
    print(f"VPN/Proxy   : {vpn_proxy_detail}")
    print(f"OS          : {os_info}")
    print(f"Terminal    : {term_type}")
    print(f"User-Agent  : {user_agent_info}")
    if latency:
        print(f"Ping        : {latency} ms")

if __name__ == "__main__":
    main()
