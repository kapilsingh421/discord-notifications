import urllib3
import json
import requests
def lambda_handler(event, context):
    url="https://discord.com/api/webhooks/83456464646232/xxxxxxxxxxxxxxxxxxxxx"
    print(event['detail'])
    data = {
        "content" : f"Detail: {event['detail']}",
        "username" : "CodebuildStatus"
    }
    headers = {
    "Content-Type": "application/json"
    }
    result = requests.post(url, json=data,headers=headers)
    if 200 <= result.status_code < 300:
        print(f"Webhook sent {result.status_code}")
    else:
        print(f"Not sent with {result.status_code}, response:\n{result.json()}")
