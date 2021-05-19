from pymongo import MongoClient
import sys,os
sys.path.append(os.getcwd())

DATABASE = MongoClient()['weather_tracker'] # DB_NAME
DEBUG = False
mongo_host=True
if(mongo_host):
    client = MongoClient("mongodb://my_db:27017")
else:
    client = MongoClient('localhost', 27017)

