import operator


class Suggestion:

    def __init__(self, db):
        self.db = db

    def get(self, name, latitude=None, longitude=None):

        cities = self.db.get(name)

        for city in cities:
            city.compute_score(name, latitude, longitude)

        cities.sort(key=operator.attrgetter('score'), reverse=True)

        return {'suggestions': [city.to_json() for city in cities]}

