from django.db import models

import requests

API_KEY = "b62fc7bb-4b86-4a2b-84bf-e6804fa32f39",
LOCATION = 'Keele'

# Make the request to the API
response = requests.get(f'https://api.bbcweather.co.uk/location/{LOCATION}/3dayforecast?api_key={API_KEY}')

# Check that the request was successful
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
else:
    print('An error occurred while retrieving the weather data')
