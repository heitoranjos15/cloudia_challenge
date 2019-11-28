from flask_api import status
from flask_restful import Resource, abort
from flask import request

from src.builders.bot_answer import get_answer
from src.builders.user import build_user
from src.queries.user import create_or_update_user
from src.queries.interactions import insert_interaction


class Answer(Resource):
    def post(self):
        quote = request.get_json(force=True).get('quote')
        user_data = request.get_json(force=True).get('user')
        answer = str()
        try:
            answer = get_answer(quote)
            user = create_or_update_user(build_user(user_data))
            insert_interaction(user, quote, answer)
        except TypeError:
            abort(status.HTTP_400_BAD_REQUEST, message="quote is invalid")
        except AttributeError:
            abort(status.HTTP_400_BAD_REQUEST, message="user is invalid")
        except Exception as e:
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR,
                  message="Internal server error", details=e)
        return {'answer': answer}
