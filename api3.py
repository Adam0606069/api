import requests

response=requests.get("https://randomfox.ca/floof")
# print(response.json())

if response.status_code==200:
    # res=response.text
    # print("response: ")
    # print(res)
    # print("json: ")
    json=response.json()
    # print(json)
    for key in json:
        print(f"{key} : {json[key]}")