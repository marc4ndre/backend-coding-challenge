import operator


class Suggestion:
    """
    Suggestion class is used to return the result of the uri /suggestions
    It receives a database to search in for cities result
    """

    def __init__(self, db):
        self.db = db

    def get(self, name, latitude=None, longitude=None):
        """
        Return a suggestion of city(ies) depending of the query with a score
        depending of the match between the suggestion and what's in the database
        :param name: suggestion name (string)
        :param latitude: latitude (float)
        :param longitude: longitude (float)
        :return:
        """

        cities = self.db.get(name)

        for city in cities:
            city.compute_score(name, latitude, longitude)

        cities.sort(key=operator.attrgetter('score'), reverse=True)

        return {'suggestions': [city.to_json() for city in cities]}

