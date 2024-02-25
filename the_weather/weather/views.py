from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    api_key = 'a5b0751817608ebcbbe1550b9603f114'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    weather_data = []

    for city in cities:
        city_name = city.name
        city_weather = requests.get(url.format(city_name, api_key)).json()

        weather = {
            'city': city_name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)
