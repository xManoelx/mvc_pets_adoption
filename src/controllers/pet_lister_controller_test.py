from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository: 
    
    # Simulates a repository for managing pet data
    def list_pets(self):
        return [
            PetsTable(id=1, name="Buddy", type="Dog"),
            PetsTable(id=2, name="Fluffy", type="Cat"),
        ]
    
# Test function to verify the pet listing functionality
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list_pets()

    expected_response = {
        'data': {
                'type': 'Pets',
                'count': 2,
                'attributes': [
                    {'name': 'Buddy', 'type': 'Dog', 'id': 1},
                    {'name': 'Fluffy', 'type': 'Cat', 'id': 2},
                ]
            }
    }

    assert response == expected_response