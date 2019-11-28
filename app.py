from flask import Flask
from sqlalchemy import create_engine
from flask_restful import Api
from flask_migrate import Migrate


from src.routes import add_routes
from src.error_handler import blueprint
from src.builders.db_client import db


def create_app(enviroment):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = enviroment.db_host
    app.engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    api = Api(app)
    add_routes(api)
    app.register_blueprint(blueprint)

    from src.models.interactions import Interaction
    from src.models.user import User
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    return app
