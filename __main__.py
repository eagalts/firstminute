from core.check import Check
from core.status import Status

check = Check(status=Status.CRIT, message="Demo Critical Error", listOfChecks=[Check(status=Status.LOW, message="Demo Low Error")])
print("> ", check.status)
print("  ", check.message)
print("   * ", check.listOfChecks[0].status)
print("   * ", check.listOfChecks[0].message)