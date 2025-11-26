import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()

# Teste para listar pets
@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

# Teste para deletar um pet
@pytest.mark.skip(reason="interacao com o banco de dados")
def test_delete_pets():
    name = "belinha"

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

# Teste para inserir uma pessoa
@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_person():
    first_name = "Ricardo"
    last_name = "Costa"
    age = 30
    pet_id = 1

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

# Teste para inserir uma pessoa
@pytest.mark.skip(reason="interacao com o banco de dados")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print('----------------------------------------')
    print(response)
    print(response.pet_name)
    print('----------------------------------------')
