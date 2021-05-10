from flask import Flask
from flask_restful import Api
from src.views.hello import HelloWorld
from src.views.agent import CitiesList,AddCityEndpoint,RemoveCityEndpoint,GetCityWeatherData

app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API

api.add_resource(CitiesList, '/weather_agent/get_cities')
api.add_resource(AddCityEndpoint, '/weather_agent/add_city')
api.add_resource(RemoveCityEndpoint, '/weather_agent/delete_city')
api.add_resource(GetCityWeatherData, '/weather_agent/get_city_weather_data')


app.run(debug=True,port=5000)                #  Start a development server