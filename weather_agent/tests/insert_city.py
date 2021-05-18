import json
import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[1])
sys.path.append(d)

from tests.BaseCase import BaseCase

class InsertCity(BaseCase):

    def test_insert_city(self):
        args=json.dumps({'city':'Larisa'})
        
        response =  self.app.post('/WeatherAgent/insert_city', headers={"Content-Type": "application/json"}, data=args)
        # Then
        print("this test is gunna fail")
        print(response.data)
        self.assertEqual(str, type(response.json['_id']))
        self.assertEqual(200, response.status_code)

    def test_wrong_input(self):
        pass
    
    def test_allready_exists(self):
        args=json.dumps({'city':'Larisa'})
        
        response =  self.app.post('/WeatherAgent/insert_city',headers={"Content-Type": "application/json"}, data=args)
        response =  self.app.post('/WeatherAgent/insert_city',headers={"Content-Type": "application/json"}, data=args)
        # Then
        print("this test is gunna fail")
        print(response.json['message'])
        self.assertEqual('City already exists', response.json['message'])
        self.assertEqual(400, response.status_code)

