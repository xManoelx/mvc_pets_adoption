
class HttpNotFoundError(Exception):
    """Exception raised for HTTP 404 Not Found errors."""

    def __init__(self, message = str) -> None:
        super().__init__(message)
        self.status_code = 404
        self.name = "Not Found"
        self.message = message