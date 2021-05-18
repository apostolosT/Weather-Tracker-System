import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[2])
sys.path.append(d)

from typing import List
from flask_restful import Resource, reqparse
from flask import request
from flask import current_app as app
import requests
from src.weather_agent.storage import Mongo
import pymongo

# 

class City(Resource):
    def __init__(self) -> None:
        self.db = Mongo(app.config["DB_URI"])
        self.coll = "Cities"
        self.db_name = app.config["DB_NAME"]

    def post(self):
        
        args=request.get_json(force=True)
        try:
            x=self.db.insert_city(self.db_name, self.coll, args)
            if(x):
                print(f"{(args['city'])} city added")
                return {'_id':x.inserted_id},200
      
        except pymongo.errors.DuplicateKeyError:
            # return f"{args['city']} city already exists",400
            return {"message":"City already exists"},400
    
    def delete(self,city:dict):

        
        res=self.db.delete_city(self.db_name,self.coll,city)

        if(res):
            return {"message":f"{city} city deleted"},200
        else:
            return {"message":f"{city} city not found"},404
    

class Cities(City):
    
    def get(self):
       cities=self.db.find_cities(self.db_name, self.coll)
       return cities

class GetCityWeatherData(Resource):
    def __init__(self) -> None:
        self.db = Mongo(app.config["DB_URI"])
        self.coll = "Cities"
        self.db_name = app.config["DB_NAME"]
        self.url = 'http://0.0.0.0:5200/weather_service/current-weather'
    
    
    
    def post(self):
        cities=self.db.find_cities(self.db_name, self.coll)
       
        # cities:List[str]=[city for city in cities.values()]
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='form')

        args = parser.parse_args(strict=True)
        # print(args['city'])

        if args['city'] in cities['cities'] :
            x = requests.post(self.url, data = args)
            x=x.json()
            # weather_data_collection.insert_one(x)
            
            return x
        
        else:
            return (f"Cannot fetch weather data for {args['city']} city. It is not listed in tracked cities. \n")