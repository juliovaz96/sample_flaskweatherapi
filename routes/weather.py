from flask import Blueprint, jsonify, request
from services.weather_service import get_weather
from config import Config

# Create a blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather', methods=['GET'])
def get_weather_route():
    """
    API endpoint to get weather information for a specified city.
    
    Query Parameters:
    city (str): The city name (default is Toronto).
    
    Returns:
    JSON: Weather information or an error message if the city is not found.
    """
    city = request.args.get('city', default='Toronto')
    api_key = Config.OPENWEATHER_API_KEY
    weather_data = get_weather(city, api_key)
    
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({"error": "City not found"}), 404
