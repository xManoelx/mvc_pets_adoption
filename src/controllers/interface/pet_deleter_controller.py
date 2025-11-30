from typing import Dict 
from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):
        
    @abstractmethod
    def delete(self, pet_info: Dict) -> Dict:
        pass