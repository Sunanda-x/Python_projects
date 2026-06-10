import requests

# Paste your API key here
api_key = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:

    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]

    print("\n========== WEATHER REPORT ==========")
    print(f"City        : {city_name}")
    print(f"Country     : {country}")
    print(f"Temperature : {temperature} °C")
    print(f"Feels Like  : {feels_like} °C")
    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")
    print(f"Condition   : {weather.title()}")
    print("====================================")

else:
    print("\nError!")
    print("City not found or API key is invalid.")
    print("Server Response:", data.get("message", "Unknown error"))