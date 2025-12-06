
class HttpBadRequestError(Exception):
    """Exception raised for HTTP 400 Bad Request errors."""

    def __init__(self, message = str) -> None:
        super().__init__(message)
        self.status_code = 400
        self.name = "Bad Request"
        self.message = message