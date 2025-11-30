from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable

class PetListerController:

    # Metodo construtor
    def __init__(self, pet_repository: PetsRepositoryInterface):
        self.__pet_repository = pet_repository

    # Metodo para listar os pets
    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    # Metodo privado para obter os pets no banco de dados
    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets
    
    # Metodo privado para formatar a resposta
    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                'name': pet.name,
                'type': pet.type,
                'id': pet.id
            })

        return {
            'data': {
                'type': 'Pets',
                'count': len(formatted_pets),
                'attributes': formatted_pets
            }
        }