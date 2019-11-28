import os
from flask_testing import TestCase

from app import create_app
from config import configs
from src.builders.db_client import db


class BaseTestCase(TestCase):

    def create_app(self):
        env = configs.get(os.environ.get('service_env', 'test'))
        app = create_app(env)
        return app

    def setUp(self):
        from src.models.interactions import Interaction
        from src.models.user import User
        db.create_all()

    def tearDowm(self):
        db.drop_all()
