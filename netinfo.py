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
    import platform
    import socket
    # Assignment variabel utama
    local_ip = get_local_ip()
    info = get_public_info()
    public_ip = info.get("ip", "-")
    isp = info.get("org", "-")
    asn = "-"
    if isp != "-":
        asn = isp.split()[0] if isp.startswith("AS") else "-"
    org = info.get("org", "-")
    region = info.get("region", "-")
    country = info.get("country", "-")
    vpn_proxy = info.get("privacy", {}).get("vpn", False) or info.get("privacy", {}).get("proxy", False)
    vpn_status = "No / Unknown" if not vpn_proxy else "Yes"
    isp_name = org.split(" ", 1)[1] if org and org.startswith("AS") and len(org.split(" ", 1)) > 1 else org
    term_type = os.environ.get("TERM", "-")

    # IP Version
    ip_version = "IPv4" if "." in public_ip else "IPv6"
    # Organization (ISP name)
    organization = isp_name
    # Reverse DNS
    try:
        reverse_dns = socket.gethostbyaddr(public_ip)[0]
    except Exception:
        reverse_dns = "-"
    # Network Type (estimasi dari ASN/org)
    network_type = "Unknown"
    if organization:
        org_lower = organization.lower()
        if any(x in org_lower for x in ["telkomsel", "indosat", "xl", "tri", "smartfren", "mobile"]):
            network_type = "Mobile"
        elif any(x in org_lower for x in ["fiber", "indihome", "biznet", "myrepublic", "iconnet"]):
            network_type = "Fiber"
        elif any(x in org_lower for x in ["dsl", "speedy"]):
            network_type = "DSL"
        elif any(x in org_lower for x in ["wifi", "wireless"]):
            network_type = "Wireless"
        else:
            network_type = "ISP"
    os_name = platform.system()
    kernel = platform.release()
    arch = platform.machine()
    hostname = platform.node()
    shell = os.environ.get("SHELL", "-")

    # Output versi 2.1.0
    print("User Network Info\n-----------------")
    print(f"Public IP    : {public_ip}")
    print(f"Local IP     : {local_ip}")
    print(f"IP Version   : {ip_version}")
    print(f"ASN          : {asn}")
    print(f"Organization : {organization}")
    print(f"Reverse DNS  : {reverse_dns}")
    print(f"Network Type : {network_type} (estimated from ASN)")
    print("\nSystem Info\n-----------")
    print(f"OS           : {os_name}")
    print(f"Kernel       : {kernel}")
    print(f"Architecture : {arch}")
    print(f"Hostname     : {hostname}")
    print(f"Terminal     : {term_type}")
    print(f"Shell        : {shell}")
    print("\nPrivacy\n-------")
    print(f"VPN / Proxy  : {vpn_status}")

    return

if __name__ == "__main__":
    main()
