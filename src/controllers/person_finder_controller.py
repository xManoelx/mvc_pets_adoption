from typing import Dict 
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from .interface.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    # Metodo construtor
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    # Metodo para encontrar uma pessoa pelo ID
    def find (self, person_info: int) -> Dict:
        person = self.__find_person_in_db(person_info)
        response = self.__format_response(person)
        return response

    # Metodo privado para encontrar a pessoa no banco de dados
    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise Exception("Pessoa nao encontrada.")
        return person

    # Formata a resposta
    def __format_response(self, person: PeopleTable) -> Dict:
        return {
            'data':{
                'type': 'person',
                'count': 1,
                'attributes': {
                    'first_name': person.first_name,
                    'last_name': person.last_name,
                    'pet_name': person.pet_name,
                    'pet_type': person.pet_type
                }
            }
        }
