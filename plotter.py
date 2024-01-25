# Functions to plot the weather forecast and history

import matplotlib.pyplot as plt
import config
import requests

key = config.weather_api

def get_history(time):
    try:
        url = "http://api.weatherapi.com/v1/history.json"
        parameters = {
            "key": key,
            "q": "Helsinki",
            "dt": time
        }
        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            print("Successfully retrieved data")
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Requests exception: {e}")
        return None
    
def get_temperatures(time):
    data = get_history(time)
    if data is None:
        print("Failed to retrieve API data")

    else:
        forecast = data["forecast"]["forecastday"]
        hourly = forecast["hour"]