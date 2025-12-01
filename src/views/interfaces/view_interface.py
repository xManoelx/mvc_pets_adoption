from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):

    @abstractmethod # Decorator que indica que o metodo deve ser implementado pelas classes filhas
    # Metodo abstrato para lidar com a requisicao HTTP
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass