from flask import Flask
from flask_restful import Api
from src.resources.agent import CitiesList,AddCityEndpoint,RemoveCityEndpoint,GetCityWeatherData
from jobs.backround_job import collect_daily_weather_data
from src.common.swagger import Swagger
from flask_cors import CORS

app = Flask(__name__)                  #  Create a Flask WSGI application
CORS(app)
api = Api(app)                         #  Create a Flask-RESTPlus API


swagger = Swagger()
app.register_blueprint(swagger.connect_swagger())

api.add_resource(CitiesList, '/weather_agent/get_cities')
api.add_resource(AddCityEndpoint, '/weather_agent/add_city')
api.add_resource(RemoveCityEndpoint, '/weather_agent/delete_city')
api.add_resource(GetCityWeatherData, '/weather_agent/get_city_weather_data')

#create backround job for collecting weather data
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
scheduler = BackgroundScheduler()
# trigger= CronTrigger(second=15)
# job = scheduler.add_job(collect_daily_weather_data,'interval',seconds=60 )
# Runs daily at 5:30 (am) 
#job=scheduler.add_job(job_function, 'cron', hour=5, minute=30)

# scheduler.start()


app.run(host='0.0.0.0',debug=True,port=5000)                #  Start a development server