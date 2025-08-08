import requests

# Replace with your own free API key from OpenWeatherMap
API_KEY = "your_api_key_here"
city = "Lagos"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Make GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
else:
    print("Error fetching data:", response.status_code)