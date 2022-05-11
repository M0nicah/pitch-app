import os
class Config():

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '') 
    # replace(
    #     'postgres://', 'postgresql://') or\
    #     'sqlite:///' + os.path.join(basedir, 'app.db')


class ProdConfig(Config):
    
    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}