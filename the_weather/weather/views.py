from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    api_key = 'YOUR_API'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + api_key

    cities = City.objects.all()
    form = CityForm(request.POST)  # Move the form instantiation outside of the if statement

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']

            # Check if the city exists by making an API request
            city_weather = requests.get(url.format(city_name)).json()

            if 'main' in city_weather:
                # City exists, proceed to save to database
                form.save()
            else:
                # City doesn't exist or API response is invalid
                form.add_error('name', f"Error: City '{city_name}' doesn't exist or API response is invalid.")
        
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        if 'main' in city_weather:
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        else:
            print(f"Skipping {city} due to missing 'main' key in API response")

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)
