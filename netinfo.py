#!/usr/bin/env python3
import socket
import requests
import json
import os
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Tampilkan info jaringan user.")
    parser.add_argument('--json', action='store_true', help='Output dalam format JSON')
    parser.add_argument('--short', action='store_true', help='Output singkat: IP publik & kota')
    parser.add_argument('--public-only', action='store_true', help='Hanya tampilkan IP publik')
    parser.add_argument('--anon', action='store_true', help='Output anonim: hanya kota & negara, tanpa IP')
    parser.add_argument('--safe-demo', action='store_true', help='Output demo: IP publik diganti contoh, aman dibagikan')
    parser.add_argument('-v', '--version', action='store_true', help='Tampilkan versi netinfo')
    args = parser.parse_args()

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
    loc = f"{city}, {region}, {country}" if city != "-" else f"{region}, {country}"
    timezone = info.get("timezone", "-")
    user_agent = get_user_agent()
    vpn_proxy = info.get("privacy", {}).get("vpn", False) or info.get("privacy", {}).get("proxy", False)
    vpn_status = "Yes" if vpn_proxy else "No/Unknown"

    data = {
        "public_ip": public_ip,
        "local_ip": local_ip,
        "isp": org,
        "location": loc,
        "city": city,
        "region": region,
        "country": country,
        "timezone": timezone,
        "asn": asn,
        "vpn_proxy": vpn_status,
        "user_agent": user_agent
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
        print(f"Location    : {loc}")
        print(f"Timezone    : {timezone}")
        print(f"ASN         : {asn}")
        print(f"VPN/Proxy   : {vpn_status}")
        print(f"User-Agent  : {user_agent}")
        return
    elif args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    elif args.short:
        print(f"{public_ip} | {city}")
        return
    elif args.public_only:
        print(public_ip)
        return

    # Output default lengkap
    print("User Info\n---------")
    print(f"Public IP   : {public_ip}")
    print(f"Local IP    : {local_ip}")
    print(f"ISP         : {org}")
    print(f"Location    : {loc}")
    print(f"Timezone    : {timezone}")
    print(f"ASN         : {asn}")
    print(f"VPN/Proxy   : {vpn_status}")
    print(f"User-Agent  : {user_agent}")

if __name__ == "__main__":
    main()
