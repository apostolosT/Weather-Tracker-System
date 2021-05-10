from flask_restful import Resource, reqparse
from flask import jsonify,request
import requests
import pymongo

import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[3])
sys.path.append(d)

from commons.db import client

# Select the database
db = client['weather_tracker']
# Select the collection
weather_data_collection = db['weather_data']
cities_collection=db['cities']

# cities=['Volos','Larisa','Athens','Thessaloniki']

class CitiesList(Resource):
    def get(self):
        cities=cities_collection.find()
        return jsonify([city for city in cities])



#add_a_city endpoint
class AddCityEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='query')
        args = parser.parse_args(strict=True)
        try:
            cities_collection.insert({"_id":args['city']})
            return (f"{args['city']} city added. \n")
        except pymongo.errors.DuplicateKeyError:
            return f"{args['city']} city already exists in database.\n"


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='form')
        args = parser.parse_args(strict=True)
        try:
            cities_collection.insert({"_id":args['city']})
            return (f"{args['city']} city added. \n")
        except pymongo.errors.DuplicateKeyError:
            return f"{args['city']} city already exists in database.\n"



class RemoveCityEndpoint(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='form')
        args = parser.parse_args(strict=True)
    
        res=cities_collection.find_one_and_delete({"_id":args['city']})
        if(res):
            return (f"{args['city']} city deleted \n")
        else:
            return (f"{args['city']} city not found")

class GetCityWeatherData(Resource):
    
    url = 'http://127.0.0.1:5200/current-weather'
    cities=cities_collection.find()

    def get(self):
        args=request.args.to_dict()  
        x = requests.post(self.url, data = args)

        if args['city'] in [city['_id'] for city in self.cities]:
            x = requests.post(self.url, data = args)
            return x.json()
        else:
            return (f"Cannot fetch weather data for {args['city']} city. It is not listed in tracked cities \n")
    

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='form')
        parser.add_argument(
            'unit',
            required=True,
            choices=('metric', 'imperial'),
            location='form',
            help='Invalid Unit: {error_msg}',
        )
        args = parser.parse_args(strict=True)

        if args['city'] in [city['_id'] for city in self.cities]:
            x = requests.post(self.url, data = args)
            
            return x.json()
        
        else:
            return (f"Cannot fetch weather data for {args['city']} city. It is not listed in tracked cities. \n")
