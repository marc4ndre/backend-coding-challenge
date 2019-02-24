

class City:
    """
    City class contains the following attributes:

    name: city name. format is city, state/province, country (string)
    latitude: latitude position (float)
    longitude: longitude position (float)
    score: score computed when a suggestion request is made (float)
    """

    def __init__(self, name, latitude, longitude, state_province, country):
        self.name = name + ', ' + state_province + ', ' + country
        self.latitude = latitude
        self.longitude = longitude
        self.score = 0

    def compute_score(self, name, latitude, longitude):
        """
        One third of the score goes for name, latitude and longitude respectively.
        :param name: city suggestion received
        :param latitude: latitude suggestion received
        :param longitude: longitude suggestion received
        :return:
        """
        ratio = 1 / 3

        self.score = len(name) / len(self.name) * ratio

        if latitude is not None:
            pct = abs(latitude - self.latitude) / self.latitude
            pct = min(max(pct, 0), 1)
            self.score += (1 - pct) * ratio

        if longitude is not None:
            pct = abs(longitude - self.longitude) / self.longitude
            pct = min(max(pct, 0), 1)
            self.score += (1 - pct) * ratio

    def to_json(self):
        """
        Convert a city object to json
        :return: json
        """
        return {'name': self.name,
                'latitude': self.latitude,
                'longitude': self.longitude,
                'score': self.score}

