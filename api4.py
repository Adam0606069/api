import requests

base_url="https://httpbin.org"
headers={"User-Agent": "horada"}
payload={"firstName": "Chris P.", "lastName": "Bacon"}

res=requests.get(base_url+"/get?test=pro", params=payload)
# print(res.text)
json=res.json()
for key in json:
    print(f"{key} : {json[key]}")