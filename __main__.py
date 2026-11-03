from agent.demo_check import demo_check
from core.check import Check
from core.status import Status
from checks.meminfo import check_meminfo

check = check_meminfo()
print("> ", check.name)
print("  ", check.status)
print("  ", check.message)
for item in check.listOfChecks:
    print("   * ", item)