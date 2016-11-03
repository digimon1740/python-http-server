def send(wfile, docRoot, path):
    with open(docRoot + path, 'r', encoding='ascii', errors='ignore') as file:
        lines = file.readlines()
        line = ''
        for line in lines:
            wfile.write(bytes(line, "utf8"))


def send_status():
    pass


def send_error():
    pass
