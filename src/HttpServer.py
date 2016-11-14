import time

from src.utils import YamlParser
from src.utils import banner

from http.server import HTTPServer
import socketserver
import threading

from src.http import HttpServerHandler
from src.http import ShutdownHandler

from src.exception import ShutdownException
import sys

class HttpServerRunner(threading.Thread):
    def run(self):
        server_config = YamlParser.get("Server")

        bind_port = server_config['port']

        try:
            # initialized Http Handler
            server = HTTPServer(('', bind_port), HttpServerHandler.HttpServerHandler)
            print(time.asctime(), "Server Starts")

            banner.print_banner()
            server.serve_forever()
        except Exception as err:
            print(err)

            print(time.asctime(), "Server Stops")


class ShutdownRunner(threading.Thread):
    def run(self):
        server_config = YamlParser.get("Server")

        bind_port = server_config['shutdownPort']
        shutdown_server = None
        try:
            # initialized Shutdown Handler
            shutdown_server = socketserver.TCPServer(('', bind_port), ShutdownHandler.ShutdownHandler)
            print(time.asctime(), "Listening Shutdown.")

            shutdown_server.serve_forever()

        except ShutdownException.ShutdownException as err :
            sys.exit()
        except Exception as err:
            print(err)

            print(time.asctime(), "Server Stops")


if __name__ == "__main__":
    httpServerRunner = HttpServerRunner()
    shutdownRunner = ShutdownRunner()
    httpServerRunner.start()
    shutdownRunner.start()
