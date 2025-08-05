import requests
api_key = "5fbc77641153362923d6ab5c9c4d3972"

user_input = input("Enter city: ")
weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=imperial")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

# print(weather_data.json())
# print(weather, temp)
print(f"The weather in {user_input} is {weather}")
print(f"The temperature in {user_input} is {temp} Degrees")
