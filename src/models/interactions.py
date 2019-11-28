from datetime import datetime
from src.builders.db_client import db

class Interaction(db.Model):
    __tablename__ = 'interaction'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    quote = db.Column(db.String(280), nullable=False)
    answer = db.Column(db.String(280), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
