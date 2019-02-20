#!/usr/bin/env python
from app.rest_server import RestServer


def main():
    rest_server = RestServer()
    rest_server.run()


if __name__ == "__main__":
    main()
