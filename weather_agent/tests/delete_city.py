import json
import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[1])
sys.path.append(d)

from tests.BaseCase import BaseCase

class DeleteCity(BaseCase):

    def test_delete_city(self):
        data={'city':'Madrid'}
        args=json.dumps({'city':'Madrid'})
        self.app.post('/WeatherAgent/insert_city', headers={"Content-Type": "application/json"} ,data=args)

        response=self.app.delete('/WeatherAgent/delete_city'+f"/{data['city']}")
        mock_message=f"{data['city']} city deleted"
        
        # print(mock_message)
        # print(response)
        self.assertEqual(mock_message,response.json['message'])
        self.assertEqual(200, response.status_code)
    
    def test_not_in_db(self):
        data={'city':'Madrid'}
        args=json.dumps({'city':'Madrid'})
        self.app.post('/WeatherAgent/insert_city', headers={"Content-Type": "application/json"} ,data=args)

        self.app.delete('/WeatherAgent/delete_city'+f"/{data['city']}")
        response=self.app.delete('/WeatherAgent/delete_city'+f"/{data['city']}")

        mock_message=f"{data['city']} city not found"
        
        print(mock_message)
        print(response.data)
        self.assertEqual(mock_message,response.json['message'])
        self.assertEqual(404, response.status_code)
