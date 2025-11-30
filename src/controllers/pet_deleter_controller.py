
from .pet_lister_controller import PetListerController

class PetDeleterController:
    # Metodo Construtor
    def __init__(self, pets_repository: PetListerController) -> None:
        self.__pet_repository = pets_repository

    # Metodo para deletar um pet
    def delete_pet(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)
        