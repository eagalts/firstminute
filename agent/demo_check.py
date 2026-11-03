import os
from core.status import Status
from core.check import Check

def demo_check():
    expected = os.environ.get("EXPECTED", "OK")
    if expected not in Status.__members__:
        raise ValueError(f"Invalid expected status: {expected}")

    result_check = Check(status=Status[expected], message=f"Demo {expected} Error", listOfChecks=[Check(status=Status.LOW, message="Demo Low Error")])

    return result_check