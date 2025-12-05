from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

class MockConnection:
    # Inicializa a conexão mockada
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)], # Query result for list_pets
                    [
                        PetsTable(name='dog', type='dog'),
                        PetsTable(name='cat', type='cat')
                    ]
                )
            ]
        )

    # Funcao de entrar no contexto
    def __enter__(self): return self
    # Funcao de sair do contexto
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    # Inicializa a conexão mockada
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    # Funcao para simular resultado vazio
    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound('NoResultFound')

    # Funcao de entrar no contexto
    def __enter__(self): return self
    # Funcao de sair do contexto
    def __exit__(self, exc_type, exc_val, exc_tb): pass

# Testa a funcao list_pets do repositorio de pets
def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == 'dog'

# Testa a funcao delete_pet do repositorio de pets
def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete_pet('petName')

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == 'petName')
    mock_connection.session.delete.assert_called_once()

# Testa a funcao list_pets do repositorio de pets quando nao ha resultados
def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

# Testa a funcao delete_pet do repositorio de pets
def test_delete_pet_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pet('petName')

    mock_connection.session.rollback.assert_called_once()
