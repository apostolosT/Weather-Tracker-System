from flask import Flask
from flask_restful import Api
from flask_cors import CORS
# import os,sys
# sys.path.append(os.getcwd())

# Import Resources
from src.resources.current_weather import CurrentWeather
from src.common.swagger import Swagger

app = Flask(__name__)
CORS(app)
api = Api(app)

# Add swagger to service.
swagger = Swagger()
app.register_blueprint(swagger.connect_swagger())

api.add_resource(CurrentWeather, '/weather_service/current-weather')

app.run(host='0.0.0.0',debug=True,port=5200,threaded=True)