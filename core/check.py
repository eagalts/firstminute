from core.status import Status

class Check:
    def __init__(self, status: Status, name: str = "", message: str = "", listOfChecks: list = None):
        self.status = status
        self.name = name
        self.message = message
        self.listOfChecks = listOfChecks or []