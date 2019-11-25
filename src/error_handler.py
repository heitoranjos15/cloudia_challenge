from flask import Blueprint

blueprint = Blueprint('errors', __name__)

@blueprint.app_errorhandler(404)
def handle404():
    return '404 handled'

@blueprint.app_errorhandler(404)
def handle_type_error(e):
    return '500 handled', 500
