import socketserver

from src.utils import YamlParser
from src.http import ResponseProcessor


class HttpServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("클라이언트 접속 : {0}".format(self.client_address[0]))

        client = self.request  # client socket

        #ResponseProcessor


if __name__ == "__main__":

    server = YamlParser.get("Server")

    bindPort = server['port']
    server = None
    try:
        server = socketserver.TCPServer(
            ('', bindPort), HttpServerHandler)

        print("Http server Started ...")
        server.serve_forever()
    except Exception as err:
        print(err)

        print("Http server Stop ...")
