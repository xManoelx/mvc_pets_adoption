from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
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

# Testa a funcao list_pets do repositorio de pets
def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == 'dog'
