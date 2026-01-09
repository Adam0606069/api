import requests

parameters={"limit": 1}
response=requests.get("https://fakestoreapi.com/products", params=parameters)

if response.status_code==200:
    # res=response.text
    json=response.json()

for dict in json:
    for key in dict:
        print(f"{key}: {dict[key]} ")