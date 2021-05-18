import random
from typing import List
import sys
from pathlib import Path
import requests
import pymongo

d =str( Path(__file__).resolve().parents[1])
sys.path.append(d)
from database.db import client

# Select the database
db = client['weather_tracker']
# Select the collection
# weather_data_collection = db['weather_data']
cities_collection=db['cities']


request_url="http://127.0.0.1:5200/weather_service/current-weather"

def collect_daily_weather_data():

    cities=cities_collection.find()
    cities:List[str]=[city['_id'] for city in cities]
    
    for city in cities:
        args={'city':city}
        x = requests.post(request_url, data = args)
        x=x.json()
        datetime = x['time']['current']
        del x['time']['current']
        query={
            '_id':datetime,
            'weather':{
                'temp':x['weather']['temp']['current'],
                'hum' :x['weather']['hum']['humidity'],
            },
            'timezone': x['time']['timezone']

        }
        try:
            db[city].insert_one(query)
        except pymongo.errors.DuplicateKeyError:
            pass

        
    print(f"Background job activated: Collected weather data for cities {cities}")

# cities=['Volos','Larisa','Athens']
# temps=['23.1','41.1','15.3']
# def collect_daily_weather_data():
#     print({
#         'city':random.choice(cities),
#         'temps':random.choice(temps)
#     }


   