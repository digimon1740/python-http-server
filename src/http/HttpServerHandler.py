from src.utils import YamlParser
from src.http import ResponseProcessor

from http.server import BaseHTTPRequestHandler


class HttpServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        server = YamlParser.get("Server")
        doc_root = server['docRoot']

        ResponseProcessor.send(self.wfile, doc_root, self.path)

        return
