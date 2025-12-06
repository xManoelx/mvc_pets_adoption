import re
from typing import Dict 
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interface.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
    # Metodo construtor
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    # Metodo para criar uma pessoa
    def create(self, person_info: Dict):
        first_name = person_info['first_name']
        last_name = person_info['last_name']
        age = person_info['age']
        pet_id = person_info['pet_id']

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_response(person_info)
        return formated_response

    # Validacao dos nomes
    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressao regular para validar caracteres nao permitidos
        non_valid_caracters = re.compile(r'[^a-zA-Z]')

        if non_valid_caracters.search(first_name) or non_valid_caracters.search(last_name):
            raise HttpBadRequestError("Nome da pessoa invalido. Apenas letras sao permitidas.")

    # Insercao da pessoa no banco de dados
    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    # Formata a resposta 
    def __format_response(self, person_info: Dict) -> Dict:
        return {
            'data':{
                'type': 'person',
                'count': 1,
                'attributes': person_info
            }
        }