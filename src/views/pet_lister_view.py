from src.controllers.interface.pet_lister_controller import PetListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.controller = controller

    # Metodo abstrato para lidar com a requisicao HTTP
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.controller.list()

        return HttpResponse(status_code=200, body=body_response)