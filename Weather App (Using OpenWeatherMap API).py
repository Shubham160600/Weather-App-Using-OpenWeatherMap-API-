import requests

API_KEY = "your_api_key_here"
city = input("Enter city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url).json()

if response.get("cod") != 200:
    print("City not found.")
else:
    weather = response['weather'][0]['description']
    temp = response['main']['temp']
    print(f"Weather in {city}: {weather}, {temp}°C")
