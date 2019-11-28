from src.builders.db_client import db
from src.models.user import User
from src.models.interactions import Interaction


def create_or_update_user(user_data):
    name, plataform = user_data
    user = User(
            name=name,
            plataform=plataform
        )
    user_inserted = db.session.merge(
        user
    )
    db.session.commit()
    return user_inserted


def get_user_interactions(user_id):
    return db.session.query(User, Interaction).join(
        Interaction, User.id == Interaction.user
    ).filter(
        User.id == user_id
    ).all()
