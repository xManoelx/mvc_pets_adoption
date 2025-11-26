from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetsRepository(PetsRepositoryInterface):
    """Repositorio de pets"""

    # Método construtor
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    # Funcao para listar todos os pets
    def list_pets(self) -> List[dict]:
        """Lista todos os pets"""
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    # Funcao para deletar um pet pelo nome
    def delete_pets(self, name: str) -> None:
        """Deleta um pet pelo nome"""
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )      
                database.session.commit()   
            except Exception as exception:
                database.session.rollback()
                raise exception
