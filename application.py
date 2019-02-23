from flask import Flask
from app.rest_server import RestServer

import logging

FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
DATE_FMT = '%m/%d/%Y %H:%M:%S'

loglevel = logging.DEBUG
logging.basicConfig(format=FORMAT, datefmt=DATE_FMT, level=loglevel)

application = Flask(__name__)
rest_server = RestServer(application)
rest_server.load_db()

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

