import os
import random
from flask_testing import TestCase
from faker import Faker

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
        self.mocks_db(Interaction, User)

    def tearDowm(self):
        db.session.remove()
        db.drop_all()

    def mocks_db(self, interaction, user):
        plataform = ['twitter', 'facebook', 'instragram']
        random_users = int(random.uniform(5, 10))
        fake = Faker()
        for _ in range(random_users):
            name = fake.name()
            plataform = random.choice(plataform)
            user_created = user(name=name, plataform=plataform)
            db.session.add(user_created)
            db.session.commit()
            random_interactions = int(random.uniform(1, 5))
            for _ in range(random_interactions):
                db.session.add(interaction(quote=fake.sentence(),
                                           answer=fake.sentence(), user=user_created.id))
        db.session.commit()
