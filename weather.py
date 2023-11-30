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


# def get_temperature():
#     data = get_data()
#     data["current"]

data = get_data()
print(data)