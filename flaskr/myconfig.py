class Config(object):
    #configuration
    DATABASE = ''
    DEBUG = False
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'

class developmentConfig(Config):
    DATABASE = './flaskr.db'
    DEBUG = True

class productionConfig(Config):
    DATABASE = 'mysql:xxxxx'
    DEBUG = False
