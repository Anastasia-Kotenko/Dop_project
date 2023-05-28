import requests


def get_weather_forecast(api_key, city, days=7, hourly=False):
    if hourly:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if "cod" in data and data["cod"] == "404":
        print(f"Weather forecast for {city} not found.")
        return

    if hourly:
        forecasts = data["list"]
        print(f"Weather forecast for {city} (next {len(forecasts)} hours):")
        for forecast in forecasts:
            timestamp = forecast["dt"]
            temperature = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            wind_speed = forecast["wind"]["speed"]
            print(f"Timestamp: {timestamp}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind speed: {wind_speed} m/s")
            print("-------------")
    else:
        main_weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather forecast for {city}:")
        print(f"Main weather: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")


# # Ваш API-ключ OpenWeatherMap
# api_key = "YOUR_API_KEY"
#
# # Назва міста, для якого потрібно отримати прогноз погоди
# city_name = "Kiev"
#
# get_weather_forecast(api_key, city_name)

# Змінити місцезнаходження та розмір прогнозу
city_name = input("Введіть назву міста: ")
forecast_days = int(input("Введіть кількість днів прогнозу (6 або 7): "))
hourly_forecast = input("Отримувати прогноз по годинах? (yes або no): ").lower() == "yes"
api_key = input("Введіть api-key: ")

get_weather_forecast(api_key, city_name, forecast_days, hourly_forecast)
