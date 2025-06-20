import requests
import os
from dotenv import load_dotenv


class TemperatureHelper:
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")
        self.weather_url = os.getenv("WEATHER_URL")
        self.result = ''
        self.data = ''

    def run(self, **params):
        params['appid'] = self.weather_api_key
        response = requests.get(self.weather_url, params=params)
        self.data = response.json()

    def temperature(self):
        return f"Температура: {self.data['main']['temp']} °C"


# load_dotenv()
# city = 'Kyiv'
# weather_api_key = os.getenv("WEATHER_API_KEY")
# weather_url = os.getenv("WEATHER_URL")
# params = {
#     'q': city,
#     'appid': weather_api_key,
#     'units': 'metric'
# }
# response = requests.get(weather_url, params=params)
# data = response.json()
# temperature = f"Температура: {data['main']['temp']} °C"
