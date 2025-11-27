import pytest
from src.controllers.person_creator_controller import PersonCreatorController

# Mock repository para testes
class MockPeopleRepository:

    # Simula a inserção de uma pessoa no repositório
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

# Teste de funcao para criar uma pessoa
def test_create_person():
    person_info = {
        'first_name': "Paulo",
        'last_name': "Pedro",
        'age': 30,
        'pet_id': 1
    }
    
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response['data']['type'] == 'person'
    assert response['data']['count'] == 1
    assert response['data']['attributes'] == person_info

# Teste de funcao para criar uma pessoa com erro no nome
def test_create_person_error():
    person_info = {
        'first_name': "Pedro123",
        'last_name': "Paulo",
        'age': 30,
        'pet_id': 1
    }
    
    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_info)
