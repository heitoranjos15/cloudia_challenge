from src.views.answer import Answer
from src.views.interaction import Interaction
from src.views.user import User
from src.error_handler import blueprint


def add_routes(api):
    api.add_resource(
        Answer,
        '/answer',
        endpoint="bot_answer"
    )
    api.add_resource(
        Interaction,
        '/interaction/<int:id_interaction>',
        endpoint='bot_interactions'
    )
    api.add_resource(
        User,
        '/user/<int:id_user>/interactions',
        endpoint='user_interactions'
    )
