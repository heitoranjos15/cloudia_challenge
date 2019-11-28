from src.builders.db_client import db
from src.models.interactions import Interaction
from src.models.user import User


def insert_interaction(user, quote, answer):
    interaction = Interaction(user=user.id, quote=quote, answer=answer)
    db.session.add(
        interaction
    )
    db.session.commit()
    return interaction


def get_interaction(interaction_id):
    return db.session.query(Interaction, User).join(
        User, Interaction.user == User.id
    ).filter(
        Interaction.id == interaction_id
    ).first()
