class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True
    DB_URI = "mongodb://localhost:27017"
    DB_NAME = "weather_tracker"
