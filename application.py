#!/usr/bin/env python
from app.rest_server import RestServer

import logging
import os


def main():
    log_path = '/opt/python/log/rest_server.log'

    if not os.path.exists(os.path.dirname(log_path)):
        log_path = '/tmp/rest_server.log'

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    logging.info("Starting Rest Server!")
    rest_server = RestServer()
    rest_server.load_db()
    rest_server.run()


if __name__ == "__main__":
    main()
