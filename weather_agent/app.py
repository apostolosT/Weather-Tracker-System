from flask import Flask
from flask_restful import Api

from src.weather_agent.resources import City,Cities,GetCityWeatherData
from jobs.backround_job import collect_daily_weather_data
from src.common.swagger import Swagger
from flask_cors import CORS

app = Flask(__name__)                  #  Create a Flask WSGI application
CORS(app)
api = Api(app)     

swagger = Swagger()
app.register_blueprint(swagger.connect_swagger())                    #  Create a Flask-RESTPlus API

app.config.from_object("config.Development")

api.add_resource(City, "/WeatherAgent/insert_city","/WeatherAgent/delete_city/<city>")
api.add_resource(Cities,"/WeatherAgent/ListCities")
api.add_resource(GetCityWeatherData, '/WeatherAgent/get_city_weather_data')

# create backround job for collecting weather data
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
scheduler = BackgroundScheduler()

# Runs every 10 seconds
# job = scheduler.add_job(collect_daily_weather_data,'interval',seconds=10 )

# Runs daily at 5:30 (am) 
job=scheduler.add_job(collect_daily_weather_data, 'cron', hour=5, minute=30)

scheduler.start()

app.run(host='0.0.0.0',port=5000)                #  Start a development server