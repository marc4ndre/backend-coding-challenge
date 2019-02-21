import unittest
import os

from app.db import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_db.tsv')

    def test_load(self):
        self.db.load(self.filename)

        self.assertEqual(len(self.db.cities), 3)
        self.assertEqual(self.db.cities[0].name, 'Abbotsford, 02, CA')

    def test_get(self):
        self.db.load(self.filename)

        result = self.db.get('Abb')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Abbotsford, 02, CA')
