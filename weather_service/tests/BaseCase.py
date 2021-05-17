import unittest

import sys
from pathlib import Path
d =str( Path(__file__).resolve().parents[1])
sys.path.append(d)
from server import app

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass