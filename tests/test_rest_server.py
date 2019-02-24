import unittest
import os
from app.rest_server import RestServer


class TestRestServer(unittest.TestCase):

    def setUp(self):
        self.rest_server = RestServer()

    def test_load_db(self):
        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_db.tsv')

        try:
            self.rest_server.load_db(filename)
        except Exception as e:
            self.fail("load_db raised {} unexpectedly!".format(e))
