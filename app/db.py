import csv
import sys

from app.city import City

csv.field_size_limit(sys.maxsize)


class Database:
    """
    The database class reads the cities contained in the tsv file
    """

    def __init__(self):
        """
        Init the cities list to empty
        """
        self.cities = []

    def load(self, filename):

        with open(filename) as tsvfile:
            reader = csv.DictReader(tsvfile, dialect='excel-tab')

            for row in reader:

                self.cities.append(City(row['name'],
                                        float(row['lat']),
                                        float(row['long']),
                                        row['admin1'],
                                        row['country']))

    def get(self, name):
        """
        Rerturning all cities in a list where the city name starts with name param
        :param name: city name where searching for in cities list
        :return: all cities who starts with name
        """
        return [city for city in self.cities if city.name.lower().startswith(name.lower())]
