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
    
def get_temperatures(time = "2024-01-24"):
    data = get_history(time)
    all_hourly_temperatures = []

    if data is None:
        print("Failed to retrieve API data")
    else:
        forecast = data["forecast"]#["forecastday"]

        # Iterate through each forecast entry
        for forecast_entry in forecast["forecastday"]:
        # Access the "hour" list within each forecast entry
            hourly_temperatures = [hour_entry["temp_c"] for hour_entry in forecast_entry["hour"]]
        # Append the hourly temperatures to the overall list
            all_hourly_temperatures.extend(hourly_temperatures)

        #hourly = forecast["hour"]
        #hourly_temps = [entry["temp_c"] for entry in hourly]
        print(f"Weather history from given date: {all_hourly_temperatures}")
    return (f"Weather history from given date: {all_hourly_temperatures}")