from flask_restful import Resource
from flask import request, jsonify

from webargs import fields, validate
from webargs.flaskparser import use_kwargs, abort

import operator
import logging


class EndPoint(Resource):

    get_args = {
        "q": fields.Str(required=True),
        "latitude": fields.Float(required=False, validate=validate.Range(min=-90.0, max=90.0)),
        "longitude": fields.Float(required=False, validate=validate.Range(min=-90.0, max=90.0)),
    }

    def __init__(self, db):
        self.db = db

    @use_kwargs(get_args)
    def get(self, q, latitude=None, longitude=None):
        logging.info('GET suggestions?q={}&latitude={}&longitude={}'.format(q, latitude, longitude))

        cities = self.db.get(q)

        for city in cities:
            city.compute_score(q, latitude, longitude)

        cities.sort(key=operator.attrgetter('score'), reverse=True)

        return jsonify({'suggestions': [city.to_json() for city in cities]})
