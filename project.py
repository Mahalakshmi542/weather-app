Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import requests
... 
... def get_weather(city_name, api_key):
...     base_url = "http://api.openweathermap.org/data/2.5/weather?"
...     full_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
...     
...     response = requests.get(full_url)
...     data = response.json()
...     
...     if response.status_code == 200:
...         print(f"\nWeather in {city_name.title()}:")
...         print(f"Temperature: {data['main']['temp']}°C")
...         print(f"Humidity: {data['main']['humidity']}%")
...         print(f"Condition: {data['weather'][0]['description'].title()}")
...         print(f"Wind Speed: {data['wind']['speed']} m/s")
...     else:
...         print("City not found. Please enter a valid city name.")
... 
... if __name__ == "__main__":
...     api_key = "your_api_key_here"  # Replace with your real API key
...     city = input("Enter city name: ")
...     get_weather(city, api_key)
