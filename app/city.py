

class City:
    """
    City class
    """

    def __init__(self, name, latitude, longitude, state_province, country):
        self.name = name + ', ' + state_province + ', ' + country
        self.latitude = latitude
        self.longitude = longitude
        self.score = 0

    def compute_score(self, name, latitude, longitude):
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
        return {'name': self.name,
                'latitude': self.latitude,
                'longitude': self.longitude,
                'score': self.score}

