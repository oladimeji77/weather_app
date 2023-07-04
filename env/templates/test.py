import requests


url = "https://api.openweathermap.org/data/2.5/weather?q=Lagos&appid=37297e5381445d1294acf62440f909af"

r = requests.get(url).json()
temp = r['main']['temp']
city = r['name']
description = r['weather'][0]['description']
icon = r['weather'][0]['icon']
icon_code = f"https://openweathermap.org/img/wn/{icon}@2x.png"

print(r)
print(city)
print(type(temp))
print(description)
print(city)
print(icon)
print(icon_code)







