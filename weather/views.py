from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings


def weather_view(request):
    api_key = "494104d9d601cb6142772bd304303aaf"
    city = request.GET.get('city', 'New York')  # Default city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={api_key}&units=metric"


    response = requests.get(url)
    weather_data = response.json()

    icon_code = weather_data['weather'][0]['icon'] if 'weather' in weather_data else None

    context = {
        'city': city,
        'temperature': weather_data['main']['temp'] if 'main' in weather_data else None,
        'description': weather_data['weather'][0]['description'] if 'weather' in weather_data else None,
        'icon_url': f"http://openweathermap.org/img/wn/{icon_code}@2x.png" if icon_code else "",
    }
    return render(request, 'weather/weather.html', context)
