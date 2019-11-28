from flask_api import status
from flask_restful import Resource, abort
from flask import request

from src.queries.user import get_user_interactions


class User(Resource):
    def get(self, id_user):
        interactions = get_user_interactions(id_user)
        response_data = list()
        if not interactions:
            abort(status.HTTP_404_NOT_FOUND, message='user not found')
        for data in interactions:
            user, interactions = data
            response_data.append({
                'name': user.name,
                'plataform': user.plataform,
                'interaction': {
                    'quote': interactions.quote,
                    'answer': interactions.answer
                }
            })
        return response_data
