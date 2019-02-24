import unittest

from app.city import City


class TestCity(unittest.TestCase):

    def test_compute_score(self):
        city = City('Montreal', -90, 90, 'QC', 'CA')

        city.compute_score('Montreal', 0, 0)

        self.assertTrue(0.0 <= city.score <= 1.0)

    def test_to_json(self):
        city = City('Montreal', -90, 90, 'QC', 'CA')

        city_json = city.to_json()

        self.assertEqual('Montreal, QC, CA', city_json['name'])
        self.assertEqual(-90, city_json['latitude'])
        self.assertEqual(90, city_json['longitude'])
