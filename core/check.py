from core.status import Status

class Check:
    def __init__(self, status: Status, message: str = "", listOfChecks: list = None):
        self.status = status
        self.message = message
        self.listOfChecks = listOfChecks or []