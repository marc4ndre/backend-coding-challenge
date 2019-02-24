from flask import Flask
from app.rest_server import RestServer

import logging
import os

FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
DATE_FMT = '%m/%d/%Y %H:%M:%S'

loglevel = logging.DEBUG
logging.basicConfig(format=FORMAT, datefmt=DATE_FMT, level=loglevel)

DEFAULT_DB_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'cities_canada-usa.tsv')

application = Flask(__name__)


if __name__ == "__main__":
    rest_server = RestServer(application)
    rest_server.load_db(DEFAULT_DB_NAME)
    application.run()
