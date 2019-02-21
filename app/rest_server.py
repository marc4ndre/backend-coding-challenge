from flask import Flask
from flask_restful import Api
from app.db import Database
from app.endpoint import EndPoint

import os


class RestServer:
    DEFAULT_DB_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'cities_canada-usa.tsv')

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.database = Database()
        self.api.add_resource(EndPoint, '/suggestions', resource_class_kwargs={'db': self.database})

    def load_db(self, name=DEFAULT_DB_NAME):
        self.database.load(name)

    def run(self):
        self.app.run(debug=True)


