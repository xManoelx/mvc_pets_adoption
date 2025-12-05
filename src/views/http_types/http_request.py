from typing import Dict

class HttpRequest: 

    # Metodo construtor
    def __init__(self, body: Dict = None, params: Dict = None) -> None:
        self.body = body
        self.params = params
        
        