from agent.demo_check import demo_check
from core.check import Check
from core.status import Status

check = demo_check()
print("> ", check.status)
print("  ", check.message)
print("   * ", check.listOfChecks[0].status)
print("   * ", check.listOfChecks[0].message)