from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def createapp(config_class=Config):

    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = 'f46c992f38cf'

    # Initializing flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app