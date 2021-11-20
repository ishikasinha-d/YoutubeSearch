from flask import Flask
from .routes import main
from .extensions import mongo

def create_app(config_file='settings.py'):
    app= Flask(__name__)

    app.config.from_pyfile(config_file)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app