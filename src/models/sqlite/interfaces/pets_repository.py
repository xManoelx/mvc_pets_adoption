from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pets import PetsTable

class PetsRepositoryInterface(ABC):

    # Funcao para listar todos os pets
    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        """Lista todos os pets"""

    # Funcao para deletar um pet pelo nome
    @abstractmethod
    def delete_pets(self, name: str) -> None:
        """Deleta um pet pelo nome"""
