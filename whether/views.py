from django.shortcuts import render
import requests
from .model import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1d7ec899393d9167683b17537152d725'

    cities = City.objects.all() #return all the cities in the database

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm
    
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form':form}


    return render(request, 'weather/index.html',context) #returns the index.html template
