import time

from src.utils import YamlParser
from src.utils import banner
from src.http import ResponseProcessor

import http.server
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from urllib.parse import urlparse


class HttpServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        server = YamlParser.get("Server")
        docRoot = server['docRoot']

        ResponseProcessor.send(self.wfile, docRoot, self.path)

        return


if __name__ == "__main__":

    server = YamlParser.get("Server")

    bindPort = server['port']
    server = None
    try:
        server = HTTPServer(('', bindPort), HttpServerHandler)
        print(time.asctime(), "Server Starts")

        banner.print_banner()

        server.serve_forever()
    except Exception as err:
        print(err)

        print(time.asctime(), "Server Stops")
