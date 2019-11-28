from flask_api import status
from flask_restful import Resource, abort
from flask import request

from src.queries.interactions import get_interaction


class Interaction(Resource):
    def get(self, id_interaction):
        data_interaction = get_interaction(id_interaction)
        if not data_interaction:
            abort(status.HTTP_404_NOT_FOUND, message='interaction not found')
        interaction, user = data_interaction
        return {
            'idinteraction': interaction.id,
            'quote': interaction.quote,
            'answer': interaction.answer,
            'user': {
                'name': user.name,
                'plataform': user.plataform
            }
        }
