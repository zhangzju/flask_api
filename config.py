class Config(object):
    pass

class ProdConfig(object):
    pass

class DevConfig(object):
    debug = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:19921221@127.0.0.1:3306/flask"
    SQLALCHEMY_ECHO = False
