from django.shortcuts import render
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Nagpur'

    url = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': '7cea25bc525a55c25e65fb7bf1040959', 'units': 'metric'}

    # Make API request
    response = requests.get(url, params=PARAMS)
    data = response.json()

    # Handle errors (like invalid city name)
    if response.status_code != 200 or 'weather' not in data:
        description = "City not found"
        icon = "01d"
        temp = "-"
    else:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

    day = datetime.date.today()

    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city
    })
