import yaml


def get(key):
    stream = open("/Users/devsh/PycharmProjects/python-http-server/resources/config.yaml", 'r')
    dict = yaml.load(stream)
    return dict[key]
