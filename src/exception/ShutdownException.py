class ShutdownException(Exception):
    def __init__(self, arg):
        super().__init__('Shutdown Server Request IP : {0}'.format(arg))