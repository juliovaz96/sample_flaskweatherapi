import unittest
from app import app

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_weather(self):
        # Send a GET request to the /weather endpoint
        response = self.app.get('/weather?city=Toronto')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = response.get_json()
        
        # Check that the response contains the expected keys
        self.assertIn('city', data)
        self.assertIn('temperature', data)
        self.assertIn('description', data)
        
        # Check that the values are correct for the default city
        self.assertEqual(data['city'], 'Toronto')

if __name__ == '__main__':
    unittest.main()
