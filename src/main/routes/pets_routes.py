from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pets_lister_composer import pets_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer

pet_route_bp = Blueprint('pets_routes', __name__)

# Rota GET para listar todos os pets
@pet_route_bp.route('/pets', methods=['GET'])

# Função para listar todos os pets
def list_pets():
    view = pets_lister_composer()
    http_request = HttpRequest()
    http_respose = view.handle(http_request)
    return jsonify(http_respose.body), http_respose.status_code 

# Rota DELETE para deletar um pet pelo nome
@pet_route_bp.route('/pets/<name>', methods=['DELETE'])

# Função para deletar um pet pelo nome
def delete_pet(name):
    http_request = HttpRequest(params={'name': name})
    view = pet_deleter_composer()
    http_respose = view.handle(http_request)
    return jsonify(http_respose.body), http_respose.status_code