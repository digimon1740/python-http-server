import yaml


def get(key):
    stream = open("../resources/config.yaml", 'r')
    dict = yaml.load(stream)
    return dict[key]
