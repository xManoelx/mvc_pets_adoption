from src.controllers.interface.person_creator_controller import PersonCreatorControllerInterface
from src.validators.person_creator_validator import person_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.controller = controller

    # Metodo abstrato para lidar com a requisicao HTTP
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request)
        
        person_info = http_request.body
        body_response = self.controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
