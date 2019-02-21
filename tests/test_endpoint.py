import unittest
import os
from app.rest_server import RestServer

from app.endpoint import EndPoint
from app.db import Database


class TestEndPoint(unittest.TestCase):

    def setUp(self):
        self.app = RestServer().app.app.test_client()
        self.db = Database()
        self.filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_db.tsv')
        self.db.load(self.filename)
        self.endpoint = EndPoint(self.db)

    def test_get_name(self):
        result = self.app.get('Abb')

        self.assertEqual(result[0].name, 'Abbotsford')

    def test_get_name_with_params(self):
        pass