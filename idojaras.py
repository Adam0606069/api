
######################
# Budapest időjárása #
######################

import requests

#1. geolokáció
url="http://api.openweathermap.org/geo/1.0/direct"
my_appid="a7a8fd8d3706c594b72b83e890139c71"
payload = {"q": "Budapest", "limit": 5, "appid": my_appid}

response = requests.get(url, params=payload)
if response.status_code == 200:
    json=response.json()
    lat=json[0]['lat']
    lon=json[0]['lon']
    #print(f"lat: {lat}; lon: {lon}")


#2. időjárás megállapítása
url="https://api.openweathermap.org/data/2.5/weather"
payload={"lat": "lat", "lon": "lon", "units": "metric", "appid": my_appid}

response = requests.get(url, params=payload)
if response.status_code == 200:
    json=response.json()

   

    akt_homerseklet = json['main']['temp']
    min_homerseklet = json['main']['temp_min']
    max_homerseklet = json['main']['temp_max']
    wind_speed = json['wind']['speed']

    print(f"{min_homerseklet} <= {akt_homerseklet} <= {max_homerseklet} Celsius;\nSzél: {wind_speed}m/s")

