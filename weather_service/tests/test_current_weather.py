from BaseCase import BaseCase

from unittest import mock
import requests


class CurrentWeatherTest(BaseCase):
    @mock.patch('requests.post')
    def test_get_current_weather_city_success(self, mocked_get):
        # Arrange
        mocked_get.return_value.json.return_value = {
            'coord': {'lon': 9.177, 'lat': 48.7823},
            'weather': [
                {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}
            ],
            'base': 'stations',
            'main': {
                'temp': 3.9,
                'feels_like': -1.65,
                'temp_min': 3.33,
                'temp_max': 4.44,
                'pressure': 1011,
                'humidity': 45,
            },
            'visibility': 10000,
            'wind': {'speed': 9.26, 'deg': 270},
            'rain': {'1h': 0.82},
            'clouds': {'all': 75},
            'dt': 1617718308,
            'sys': {
                'type': 1,
                'id': 1274,
                'country': 'DE',
                'sunrise': 1617684622,
                'sunset': 1617732035,
            },
            'timezone': 7200,
            'id': 2825297,
            'name': 'Volos',
            'cod': 200,
        }

        city = 'Volos'
        

        # Act
        response = self.app.post(
            '/weather_service/current-weather',data={'city':city})
        

        # Assert
        self.assertEqual(response.json['city_name'], city)
        self.assertIs(type(response.json['weather']['icon']), str)
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