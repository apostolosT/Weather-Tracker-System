from flask import Flask
from flask_restful import Api
from src.resources.hello import HelloWorld

app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API


api.add_resource(HelloWorld, '/weather_agent/')


app.run(debug=True,port=5200)                #  Start a development server