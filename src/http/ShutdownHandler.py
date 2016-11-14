import socketserver
from src.exception import ShutdownException
from src.utils import YamlParser

import sys
class ShutdownHandler(socketserver.BaseRequestHandler):
    def handle(self):
        sock = self.request

        rbuff = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        received = received.replace('\r\n', '')

        server_config = YamlParser.get("Server")
        shutdown_command = server_config['shutdownCommand']

        print('input command {0}'.format(received), end="")
        print('shutdownCommand {0}'.format(shutdown_command))

        print("equals : {0}".format(received == shutdown_command))
        if received == shutdown_command:
            sys.exit()
    # raise ShutdownException.ShutdownException(self.client_address[0])
