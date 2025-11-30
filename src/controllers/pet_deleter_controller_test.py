from src.controllers.pet_deleter_controller import PetDeleterController

# Test function to verify the pet deletion functionality
def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleterController(mock_repository)
    
    # Nome do pet a ser deletado
    controller.delete_pet("Buddy") 
    
    # Verifica se o metodo delete_pet foi chamado uma unica vez com o nome correto
    mock_repository.delete_pet.assert_called_once_with("Buddy") 

