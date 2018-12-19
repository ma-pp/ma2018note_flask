from flask import Flask, Blueprint
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


api = Api()
db = SQLAlchemy()
migrate = Migrate()

from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint, title='Note API')

    app.register_blueprint(blueprint)

    return app

from .models import *

from .note.resources import api as noteApi

api.add_namespace(noteApi, path='/api')
