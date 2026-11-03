from agent.demo_check import demo_check
from core.check import Check
from core.status import Status
from checks.meminfo import check_meminfo

check = check_meminfo()
print("> ", check.name)
print("  ", check.status)
print("  ", check.message)
print("   * ", check.listOfChecks[0])
print("   * ", check.listOfChecks[1])
print("   * ", check.listOfChecks[2])