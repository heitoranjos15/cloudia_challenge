from flask_api import status
from flask_restful import Resource, abort
from flask import request

from src.builders.bot_answer import getAnswer


class Answer(Resource):
    def post(self):
        try:
            quote = request.get_json(force=True).get('quote')
            answer = getAnswer(quote)
            return {'answer': answer}
        except TypeError:
            abort(status.HTTP_400_BAD_REQUEST, message= "quote is invalid")
        except Exception as e:
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR,
                  message="Internal server error", details= e)
