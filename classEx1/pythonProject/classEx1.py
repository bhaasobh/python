from dataclasses import dataclass, field
from typing import Dict, List
import requests

@dataclass
class HourlyData:
    time: str
    temperature: float

class CityWeather:
    def __init__(self, city_name: str, latitude: float, longitude: float):
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.hourly = {}

    def add_dates(self, start_date, end_date):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m&start_date={start_date}&end_date={end_date}"

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from API: {response.status_code}")

        json_data = response.json()
        hourly_data = json_data["hourly"]
        print(json_data)

        for time, temperature in zip(hourly_data["time"], hourly_data["temperature_2m"]):
            date_part, time_part = time.split("T")
            year, month, day = map(int, date_part.split("-"))
            hour = int(time_part.split(":")[0])

            if year not in self.hourly:
                self.hourly[year] = {}
            if month not in self.hourly[year]:
                self.hourly[year][month] = {}
            if day not in self.hourly[year][month]:
                self.hourly[year][month][day] = []

            self.hourly[year][month][day].append(HourlyData(time=time, temperature=temperature))

    def __getitem__(self, key):
        print('__getitem__', key)



if __name__ == "__main__":
    city_weather = CityWeather(city_name="Jeruz", latitude=31.7683, longitude=35.2137)
    city_weather.add_dates(start_date="2024-01-01", end_date="2024-01-04")
    print(city_weather.city_name)
    print(city_weather)
