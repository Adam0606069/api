import requests
url='https://httpbin.org/post'
files={'file': open('api1.py', 'rb')}

response=requests.post(url, files=files)
print(response.text)