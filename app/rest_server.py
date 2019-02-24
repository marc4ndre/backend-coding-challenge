from flask_restful import Api
from app.db import Database
from app.endpoint import EndPoint


class RestServer:

    def __init__(self, application=None):
        self.application = application
        self.api = Api(self.application)
        self.database = Database()
        self.api.add_resource(EndPoint, '/suggestions', resource_class_kwargs={'db': self.database})

    def load_db(self, name):
        self.database.load(name)


