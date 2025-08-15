import requests
import datetime
import os
r = requests.get("https://ipinfo.io/ip")
public_ip = r.text
ZONE_ID=os.getenv("ZONE_ID")
API_KEY=os.getenv("API_KEY")
HOSTNAME=os.getenv("HOSTNAME")

url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
r = requests.get(url, headers=headers).json()
print(r)
dns_records = r['result']
for record in dns_records:
    if HOSTNAME in record['name']:
        url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{record['id']}"
        payload = {
            "content": f"{public_ip}",
            "name": f"{record['name']}",
            "proxied": True,
            "type": "A",
            "comment": f'last updated {datetime.datetime.now()}',
            "ttl": 1
        }
        r = requests.patch(url, json=payload, headers=headers)
        print(r.status_code)
