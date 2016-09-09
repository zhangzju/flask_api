class Config(object):
    SECRET_KEY = '79f431926b9ca77a3d61956802e39db4'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    debug = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:19921221@127.0.0.1:3306/flask"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
