import requests

def get_weather(city, api_key):
    """
    Fetches weather data for a given city using OpenWeatherMap API.

    Parameters:
    city (str): The city for which to fetch the weather.
    api_key (str): The API key for OpenWeatherMap.

    Returns:
    dict: A dictionary containing city, temperature, and weather description.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    # Send a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data['name'],
            "temperature": f"{data['main']['temp']}°C",
            "description": data['weather'][0]['description']
        }
        return weather_data
    else:
        return None
