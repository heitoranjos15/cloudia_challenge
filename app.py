from flask import Flask
from flask_restful import Api
from src.routes import add_routes
from src.error_handler import blueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mobile_recharge.db'
    api = Api(app)
    add_routes(api)
    app.register_blueprint(blueprint)
    return app
