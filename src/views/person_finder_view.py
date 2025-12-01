from src.controllers.interface.person_finder_controller import PersonFinderControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface) -> None:
        self.controller = controller

    # Metodo abstrato para lidar com a requisicao HTTP
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.params['person_id']
        body_response = self.controller.find(person_id)

        return HttpResponse(status_code=200, body=body_response)