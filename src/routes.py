from src.views.answer import Answer
from src.error_handler import blueprint

def add_routes(api):
   api.add_resource(
        Answer,
        '/answer',
        endpoint="bot_answer"
    )