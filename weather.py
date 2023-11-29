import config
import requests
import json

key = config.weather_api

parameters = {
    "key": key,
    "q": "Helsinki",
    "aqi": "no"
}

url = "http://api.weatherapi.com/v1/current.json"
response = requests.get(url, params=parameters)

print(response.json())

# def get_temperature():
#     call = ???