import os

class Config:
    # Get the OpenWeather API key from environment variable or use a default placeholder
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'e3717591ff59b7b3bfde14262aace368')
