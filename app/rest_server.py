from flask import Flask
from flask import request, jsonify
from app.db import Database


class RestServer:

    def __init__(self):

        self.app = Flask(__name__)
        self.database = Database()
        self.database.load()

        @self.app.route('/suggestions', methods=['GET'])
        def get():
           latitude = request.args.get('latitude')
           longitude = request.args.get('longitude')
           name = request.args.get('q')

           print('name {} latitude {} longitude {}'.format(name, latitude, longitude))

           cities = self.database.get(name)

           for city in cities:
               city.compute_score(latitude, longitude)

           return jsonify(self.database.get(name, latitude, longitude))

    def run(self):
        self.app.run(debug=True)
