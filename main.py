import requests
import datetime
MY_LAT = 26.846695
MY_LANG = 80.946167


my_direct = {
    "lat": MY_LAT,
    "lon": MY_LANG,
    "formatted": 0,
}

resp = requests.get("https://api.sunrise-sunset.org/json", params=my_direct)
resp.raise_for_status()
data = resp.json()


sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

timing = (sunrise_time, sunset_time)
print(int(sunrise_time.split("T")[1].split(":")[0]))
print(int(sunset_time.split("T")[1].split(":")[0]))

time_now = datetime.datetime.now()
print(time_now.hour)