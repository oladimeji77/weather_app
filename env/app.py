import requests
from flask import Flask, render_template
from datetime import datetime

now = datetime.now()



app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid=37297e5381445d1294acf62440f909af"

    r = requests.get(url).json()
    temp = r['main']['temp']
    temp = str(temp - 273.15)
    temp = temp[:4]
    city = r['name']
    description = r['weather'][0]['description']
    icon = r['weather'][0]['icon']
    icon_code = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    current_time = now.strftime("%H:%M:%S")
    return render_template("home.html", temp=temp, description=description,icon_code=icon_code, city=city, current_time=current_time)


if __name__=="__main__":
    app.run(debug=True)
    