# pylint: disable = unused-argument
from src.controllers.person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name, last_name, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

# Mock repository para testes
class MockPeopleRepository:

    def get_person(self, person_id: int):
        return MockPerson(
            first_name = "Pedro", 
            last_name = "Paulo", 
            pet_name = "Rex", 
            pet_type = "Dog")

def test_finder_person():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)

    expected_reponse = {
            'data':{
                'type': 'person',
                'count': 1,
                'attributes': {
                    'first_name': 'Pedro',
                    'last_name': 'Paulo',
                    'pet_name': 'Rex',
                    'pet_type': 'Dog'
                }
            }
        }
    
    assert response == expected_reponse