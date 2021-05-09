from flask import Flask
from flask_restful import Api
# import os,sys
# sys.path.append(os.getcwd())

from resources.current_weather import CurrentWeather
app = Flask(__name__)
api = Api(app)


api.add_resource(CurrentWeather, '/current-weather')

app.run(port=5000)