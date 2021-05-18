import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[1])
sys.path.append(d)

import unittest

from app import app

from db import client

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = client['weather_tracker']


    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
   