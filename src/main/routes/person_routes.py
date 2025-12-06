from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer

from src.errors.error_handle import handle_errors

person_route_bp = Blueprint('person_routes', __name__)

# Rota POST para criar um novo person
@person_route_bp.route('/people', methods=['POST'])

# Função para criar todos os persons
def create_person():
    try: 
        http_request = HttpRequest(body = request.json)
        view = person_creator_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
        
# Rota GET para listar uma pessoa específica pelo ID
@person_route_bp.route('/people/<person_id>', methods=['GET'])

# Função para encontrar uma pessoa pelo ID
def find_person(person_id):
    try: 
        http_request = HttpRequest(params = {'person_id': person_id})
        view = person_finder_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception: 
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code