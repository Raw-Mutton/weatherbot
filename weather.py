import config
import requests
import json

key = config.weather_api

def get_current_data():
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        parameters = {
            "key": key,
            "q": "Helsinki",
            "aqi": "no"
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


def get_temperature():
    data = get_current_data()
    if data is None:
        print("Failed to retrieve API data")
        temperature = None
    else:
        location_stats = data["location"]
        city = location_stats["name"]
        current_stats = data["current"]
        temperature = current_stats["temp_c"]
        time = current_stats["last_updated"]
        print(f"Current temperature in {city}: {temperature}\n Updated at {time}")
    return (f"Current temperature in {city}: {temperature}\n Updated at {time}")
    

# data = get_current_data()
# print(data["current"]["temp_c"])
get_temperature()