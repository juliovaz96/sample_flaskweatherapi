from flask import Flask
from routes.weather import weather_bp

# Initialize Flask application
app = Flask(__name__)

# Register the weather blueprint
app.register_blueprint(weather_bp)

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
