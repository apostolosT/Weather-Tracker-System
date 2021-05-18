from pymongo import MongoClient
import sys,os
sys.path.append(os.getcwd())

DATABASE = MongoClient()['weather_tracker'] # DB_NAME
DEBUG = False
client = MongoClient('localhost', 27017)

