from BaseCase import BaseCase

from unittest import mock
import requests


class CurrentWeatherTest(BaseCase):
    @mock.patch('requests.post')
    def test_get_current_weather_city_success(self, mocked_get):
        # Arrange
        mocked_get.return_value.json.return_value ={
            "coord": {
                "lon": -122.08,
                "lat": 37.39
            },
            "weather": [
                {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 282.55,
                "feels_like": 281.86,
                "temp_min": 280.37,
                "temp_max": 284.26,
                "pressure": 1023,
                "humidity": 100
            },
            "visibility": 16093,
            "wind": {
                "speed": 1.5,
                "deg": 350
            },
            "clouds": {
                "all": 1
            },
            "dt": 1560350645,
            "sys": {
                "type": 1,
                "id": 5122,
                "message": 0.0139,
                "country": "US",
                "sunrise": 1560343627,
                "sunset": 1560396563
            },
            "timezone": -25200,
            "id": 420006353,
            "name": "Mountain View",
            "cod": 200
        }                         


        city = 'Volos'
        

        # Act
        response = self.app.post(
            '/weather_service/current-weather',data={'city':city})
        

        # Assert
        self.assertEqual(response.json['city_name'], city)
        self.assertEqual(response.status_code, 200)

    def test_get_current_weather_no_city_failure(self):
        # Arrange
        city = ''
        error = 'City is required.'
        code = 400
        # unit = 'metric'

        # Act
        response = self.app.post(
            '/weather_service/current-weather',data={'city':city}
        )
        

        # Assert
        self.assertEqual(response.json['error'], error)
        self.assertEqual(response.status_code, code)

    @mock.patch('requests.post')
    def test_get_current_weather_wrong_response_failure(self, mock_request):
        # Arrange
        mock_resp = requests.models.Response()
        mock_resp.status_code = 404
        mock_resp.json = {'message': 'Internal error'}
        mock_request.return_value = mock_resp
        city = 'sfdfs'
        info = 'Internal server error caused by third party api.'
        code = 500

        # Act
        response = self.app.post(
             '/weather_service/current-weather',data={'city':city}
        )

        # Assert
        self.assertEqual(response.status_code, code)