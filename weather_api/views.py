from django.shortcuts import render, redirect
from weather_api.key import api_key
import requests
import math
from datetime import datetime, timedelta
# from .models import Social

# Create your views here.

def index(request):
    return render(request, "weather_api/home.html")


def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        w_dataset = requests.get(url).json()

        try:
            # Get the current day and next 5 days' names
            # Get today's day name only
            today = datetime.now()
            current_time = today.strftime('%H:%M:%S')
            day1 = today.strftime("%A")
            day2 = (today + timedelta(days=1)).strftime("%A")
            day3 = (today + timedelta(days=2)).strftime("%A")
            day4 = (today + timedelta(days=3)).strftime("%A")
            day5 = (today + timedelta(days=4)).strftime("%A")
            day6 = (today + timedelta(days=5)).strftime("%A")
            
            
            context = {
                ####
                "city_name":w_dataset["city"]["name"],
                "city_country":w_dataset["city"]["country"],
                "wind":w_dataset['list'][0]['wind']['speed'],
                "degree":w_dataset['list'][0]['wind']['deg'], 
                "status":w_dataset['list'][0]['weather'][0]['description'],
                "cloud":w_dataset['list'][0]['clouds']['all'],
                #'date':w_dataset['list'][0]["dt_txt"],
                 'date' :datetime.fromtimestamp(w_dataset['list'][0]['dt']).strftime('%d %B %Y'),

                'date1':datetime.fromtimestamp(w_dataset['list'][0]['dt']).strftime('%d/%m').lstrip("0"),

                'date2':datetime.fromtimestamp(w_dataset['list'][8]['dt']).strftime('%d/%m').lstrip("0"),

                'date3':datetime.fromtimestamp(w_dataset['list'][16]['dt']).strftime('%d/%m').lstrip("0"),

                'date4':datetime.fromtimestamp(w_dataset['list'][24]['dt']).strftime('%d/%m').lstrip("0"),

                'date5':datetime.fromtimestamp(w_dataset['list'][32]['dt']).strftime('%d/%m').lstrip("0"),

                'date6':datetime.fromtimestamp(w_dataset['list'][39]['dt']).strftime('%d/%m').lstrip("0"),


                # New Feels Like and dt Fields
                "feels_like": round(w_dataset["list"][0]["main"]["feels_like"] - 273.0),  # Convert Kelvin to Celsius
                "dt": w_dataset["list"][0]["dt"],  # Unix timestamp


                "sunrise" : datetime.fromtimestamp(w_dataset["city"]["sunrise"]).strftime('%I:%M %p'),
                "sunset" : datetime.fromtimestamp(w_dataset["city"]["sunset"]).strftime('%I:%M %p'),


                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][0]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][0]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][8]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][8]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][16]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][16]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][24]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][24]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(w_dataset["list"][32]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(w_dataset["list"][32]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(w_dataset["list"][39]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(w_dataset["list"][39]["main"]["temp_max"] -273.0),


                "pressure":w_dataset["list"][0]["main"]["pressure"],
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "sea_level":w_dataset["list"][0]["main"]["sea_level"],


                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],
                "icon":w_dataset["list"][0]["weather"][0]["icon"],
                "icon1":w_dataset["list"][0]["weather"][0]["icon"],
                "icon2":w_dataset["list"][8]["weather"][0]["icon"],
                "icon3":w_dataset["list"][16]["weather"][0]["icon"],
                "icon4":w_dataset["list"][24]["weather"][0]["icon"],
                "icon5":w_dataset["list"][32]["weather"][0]["icon"],
                "icon6":w_dataset["list"][39]["weather"][0]["icon"],
                "day1": day1,
                "day2": day2,
                "day3": day3,
                "day4": day4,
                "day5": day5,
                "day6": day6,
                "current_time" : current_time,
            } 
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')


# def social_links(request):
#     sl = Social.objects.all()
#     context = {
#         'sl': sl
#     }
#     return render(request, 'weather_api/base.html', context)
