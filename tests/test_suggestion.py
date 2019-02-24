import unittest
import os

from app.db import Database
from app.suggestion import Suggestion


class TestSuggestion(unittest.TestCase):

    def setUp(self):

        self.filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_db.tsv')
        self.db = Database()
        self.db.load(self.filename)
        self.suggestion = Suggestion(self.db)

    def test_get_name(self):

        response = self.suggestion.get('Abb')

        self.assertEqual(len(response['suggestions']), 1)
        self.assertEqual(response['suggestions'][0]['name'], 'Abbotsford, 02, CA')
        self.assertTrue(0 >= response['suggestions'][0]['score'] <= 1)

    def test_get_name_with_params(self):
        response = self.suggestion.get('Abb', -10, 10)

        self.assertEqual(len(response['suggestions']), 1)
        self.assertEqual(response['suggestions'][0]['name'], 'Abbotsford, 02, CA')
        self.assertTrue(0 >= response['suggestions'][0]['score'] <= 1)
