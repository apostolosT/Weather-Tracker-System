from flask import Flask
from flask_restful import Api
# import os,sys
# sys.path.append(os.getcwd())

# Import Resources
from src.resources.current_weather import CurrentWeather
from src.common.swagger import Swagger

app = Flask(__name__)
api = Api(app)

# Add swagger to service.
swagger = Swagger()
app.register_blueprint(swagger.connect_swagger())

api.add_resource(CurrentWeather, '/weather_service_api/current-weather')

app.run(port=5200)