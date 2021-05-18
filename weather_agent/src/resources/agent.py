from typing import List
from flask_restful import Resource, reqparse
from flask import jsonify,request
import requests
import pymongo

import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[2])
sys.path.append(d)

from database.db import client

# Select the database
db = client['weather_tracker']
# Select the collection
weather_data_collection = db['weather_data']
cities_collection=db['cities']

#should i retrieve tracked cities from cache as well?

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
        #delete also historical data for tracked city?

        if(res):
            return (f"{args['city']} city deleted \n")
        else:
            return (f"{args['city']} city not found")

class GetCityWeatherData(Resource):
    
    url = 'http://0.0.0.0:5200/weather_service/current-weather'
    
    
    
    def post(self):
        cities=cities_collection.find()
        cities:List[str]=[city['_id'] for city in cities]

        parser = reqparse.RequestParser()
        parser.add_argument('city', location='form')

        args = parser.parse_args(strict=True)
        print(args['city'],cities)

        if args['city'] in cities :
            x = requests.post(self.url, data = args)
            x=x.json()
            # weather_data_collection.insert_one(x)
            
            return x
        
        else:
            return (f"Cannot fetch weather data for {args['city']} city. It is not listed in tracked cities. \n")
