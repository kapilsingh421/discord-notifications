import requests
import json
from collections import namedtuple

WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
names = ['www.google.com', 'www.facebook.com']
url="https://discord.com/api/webhooks/845475858/xxxxxxxxxxxxxxxxxxxxxxxx"

def get_status(site):
    try:
        response = requests.post(site, data=json.dumps({"query": '{__type(name:"Query") {name}}'}), headers={"Content-Type": "application/json"}, timeout=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = WebsiteStatus(status_code, reason)
    return website_status


for name in names:
    site = 'http://{}'.format(name)
    website_status = get_status(site)
    print("{0:30} {1:10} {2:10}"
          .format(site, website_status.status_code, website_status.reason))
          
###############################################Code to send notifications to dicsord #######################################
    data = {
        "content" : ("{0:30} {1:10} {2:10}"
          .format(site, website_status.status_code, website_status.reason)),
        "username" : "HealthCheck"
    }
    headers = {
    "Content-Type": "application/json"
    }
    result = requests.post(url, json=data,headers=headers)
    if 200 <= result.status_code < 300:
        print(f"Webhook sent {result.status_code}")
    else:
        print(f"Not sent with {result.status_code}, response:\n{result.json()}")
        
