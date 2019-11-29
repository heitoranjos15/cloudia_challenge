import os


class Development:

    def __init__(self):
        self.enviroment = 'dev'
        self.db_host = 'sqlite:///chatbot.db'


class Production:

    def __init__(self):
        self.enviroment = 'prd'
        self.db_host = 'sqlite:///chatbot.db'

class Testing:

    def __init__(self):
        self.enviroment = 'testing'
        self.db_host = 'sqlite://'

configs = {
    'dev': Development(),
    'prd': Production(),
    'test': Testing()
}
