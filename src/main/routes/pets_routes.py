from flask import Blueprint, jsonify

pet_route_bp = Blueprint('pets_routes', __name__)

# Rota GET para listar todos os pets
@pet_route_bp.route('/pets', methods=['GET'])

# Função para listar todos os pets
def list_pets():
    return jsonify({"message": "List of all pets"}), 200