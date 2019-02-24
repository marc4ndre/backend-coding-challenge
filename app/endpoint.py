from flask_restful import Resource
from flask import jsonify

from webargs import fields, validate
from webargs.flaskparser import use_kwargs, abort
from app.suggestion import Suggestion

import logging


class EndPoint(Resource):
    """
    The EndPoint class is a flask endpoint resource used when the url path is /suggestions
    """

    get_args = {
        "q": fields.Str(required=True),
        "latitude": fields.Float(required=False, validate=validate.Range(min=-90.0, max=90.0)),
        "longitude": fields.Float(required=False, validate=validate.Range(min=-90.0, max=90.0)),
    }

    def __init__(self, db):
        self.suggestion = Suggestion(db)

    @use_kwargs(get_args)
    def get(self, q, latitude=None, longitude=None):
        """
        Return a suggestion of city(ies) depending of the query with a score
        depending of the match between the suggestion and what's in the database
        :param q: suggestion name
        :param latitude: latitude received from the suggestion ( optional )
        :param longitude: longitude received from the suggestion ( optional )
        :return: json
        """

        logging.info('GET suggestions?q={}&latitude={}&longitude={}'.format(q, latitude, longitude))

        return jsonify(self.suggestion.get(q, latitude, longitude))
