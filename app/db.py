import csv
import sys
import os
from app.city import City

csv.field_size_limit(sys.maxsize)


class Database:

    DEFAULT_FILE_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cities_canada.tsv')

    def __init__(self):
        self.cities = []

    def add_city(self, name, latitude, longitude, state_province, country):
        self.cities.append(City(name, latitude, longitude, state_province, country))

    def load(self, file=DEFAULT_FILE_NAME):

        with open(file) as tsvfile:
            reader = csv.DictReader(tsvfile, dialect='excel-tab')

            for row in reader:
                self.add_city(row['name'], row['lat'], row['long'], row['admin1'], row['country'])

    def get(self, name):
        return [city for city in self.cities if city.name.lower().startswith(name.lower())]

    def compute_score(self, latitude, longitude):

        #TODO implement score
        pass
