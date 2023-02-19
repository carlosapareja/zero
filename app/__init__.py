from flask import Flask
from .config import Config
from .routes.zero import zero

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(zero)

    return app
