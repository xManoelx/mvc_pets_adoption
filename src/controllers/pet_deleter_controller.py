from .pet_lister_controller import PetListerController
from .interface.pet_deleter_controller import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    # Metodo Construtor
    def __init__(self, pets_repository: PetListerController) -> None:
        self.__pet_repository = pets_repository

   # Metodo abstrato da interface implementado
    def delete(self, pet_info: str) -> None:
        self.__pet_repository.delete_pet(pet_info)
    
    # Metodo público que chama delete
    def delete_pet(self, pet_info: str) -> None:
        self.delete(pet_info)
        