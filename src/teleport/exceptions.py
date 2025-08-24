class TeleportException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class Unreachable(TeleportException):
    def __init__(self, message: str) -> None:
        self.message = message
