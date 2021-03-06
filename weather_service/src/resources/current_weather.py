from flask_restful import Resource, reqparse
import requests
import redis 
import json

#development server
# redis_client=redis.Redis()

#docker server
redis_client=redis.Redis(host='redis', port=6379)

WEATHER_ENDPOINT='http://api.openweathermap.org/data/2.5'
KEY='56db55e7cec8ea64e84ad8e39e744f66'

class CurrentWeather(Resource):
    """
    Includes POST Method for the current weather.
    POST can get information about the current weather by city name or coordinates.
    """

    
    def post(self):
        """
        POST Method for the current weather.
        Receives city name or coordinates in the POST body.
        Also requires a valid unit.
        Returns the current weather in json format.
        See swagger for more information.
        """
        

        # Extract arguments from post request
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='form')
        parser.add_argument('daily_data_ingestion', location='form')

        # parser.add_argument('lat', type=float, location='form')
        # parser.add_argument('lon', type=float, location='form')
        # parser.add_argument(
        #     'unit',
        #     required=True,
        #     choices=('metric', 'imperial'),
        #     location='form',
        #     help='Invalid Unit: {error_msg}',
        # )
        args = parser.parse_args(strict=True)
 
 
        # Check if get current weather by city name 
        # Create url for openweather api
        if(args['city']):

            url = (
                WEATHER_ENDPOINT
                + '/weather?q='
                + args['city']
                + '&appid='
                + KEY
                + '&units=metric'
                
            )
            # check if requested data for city exist in cache
            in_cache=redis_client.get(args['city'])

            if(in_cache and args['daily_data_ingestion']!='true'):
                print(f"Weather Data for {args['city']} found in cache.")
                json_response=json.loads(in_cache)
                
                return json_response, 200

            else:
                print("Sending Request to OpenWeatherMap API")
                # Send request to openweather api
                try:
                    response_openweather = requests.get(url)
                    response_openweather.raise_for_status()
                except requests.exceptions.HTTPError as ex:
                    response_error = {
                        'info': 'Internal server error caused by third party api.',
                        'error': {
                            'code': response_openweather.status_code,
                            'message': response_openweather.reason,
                            'full_error': str(ex),
                        },
                    }
                    return response_error, 500

                # Get json from openweather response
                json_openweather = response_openweather.json()

                # Create response json
                json_response = {
                    'city_name': json_openweather['name'],
                    'weather': {
                        'main': json_openweather['weather'][0]['main'],
                        # 'description': json_openweather['weather'][0]['description'],
                        # 'icon': json_openweather['weather'][0]['icon'],
                        # 'cloudiness': json_openweather['clouds']['all'],
                        'wind': {
                            'speed': json_openweather['wind']['speed'],
                            'deg': json_openweather['wind']['deg'],
                        },
                        'temp': {
                            'current': json_openweather['main']['temp'],
                            # 'feels_like': json_openweather['main']['feels_like'],
                            # 'min': json_openweather['main']['temp_min'],
                            # 'max': json_openweather['main']['temp_max'],
                        },
                        'hum':{'humidity':json_openweather['main']['humidity']}
                    },
                    'time': {
                        'current': json_openweather['dt'],
                        'timezone': json_openweather['timezone'],
                        # 'sunrise': json_openweather['sys']['sunrise'],
                        # 'sunset': json_openweather['sys']['sunset'],
                    }
                }
                
                #saving response to cache, expire key after 10 minutes    
                redis_client.set(args['city'],json.dumps(json_response),ex=10*60)
                # Return response
                return json_response, 200
        
        else:
            response_error = {'error': 'City is required.'}
            return response_error, 400