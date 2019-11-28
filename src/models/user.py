from src.builders.db_client import db
from src.models.update_create_mixin import UpdatedCreatedMixin

class User(db.Model, UpdatedCreatedMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    plataform = db.Column(db.String(20), nullable=False)
