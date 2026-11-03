import os
from core.status import Status
from core.check import Check
from variables import GLOBAL_MEMORY_LOW, GLOBAL_MEMORY_MED, GLOBAL_MEMORY_HIGH, GLOBAL_MEMORY_CRIT

def check_meminfo():
    try:
        with open("/proc/meminfo") as file:
            meminfo = file.read()

            memTotal = 0
            memFree = 0
            memAvailable = 0

            final_status = Status.OK
            final_message = "Memory Check: Without problems"

            for line in meminfo.splitlines():
                if line.startswith("MemTotal:"):
                    memTotal = int(line.split()[1])
                elif line.startswith("MemFree:"):
                    memFree = int(line.split()[1])
                elif line.startswith("MemAvailable:"):
                    memAvailable = int(line.split()[1])
                
            if memTotal == 0:
                raise ValueError("memTotal is zero, cannot perform memory check.")

            if int(memTotal / 100 * GLOBAL_MEMORY_CRIT) > memAvailable:
                final_status = Status.CRIT  
                final_message = f"Memory Check: Less than {GLOBAL_MEMORY_CRIT}% available"
            elif int(memTotal / 100 * GLOBAL_MEMORY_HIGH) > memAvailable:
                final_status = Status.HIGH
                final_message = f"Memory Check: Less than {GLOBAL_MEMORY_HIGH}% available"
            elif int(memTotal / 100 * GLOBAL_MEMORY_MED) > memAvailable:
                final_status = Status.MED
                final_message = f"Memory Check: Less than {GLOBAL_MEMORY_MED}% available"
            elif int(memTotal / 100 * GLOBAL_MEMORY_LOW) > memAvailable:
                final_status = Status.LOW
                final_message = f"Memory Check: Less than {GLOBAL_MEMORY_LOW}% available"
            else:
                final_status = Status.OK
                final_message = f"Memory Check: OK, about {memAvailable / memTotal * 100:.2f}% available"

            check_result = Check(status = final_status, message = final_message, listOfChecks=[f"Total={memTotal}kB", f"Free={memFree}kB", f"Available={memAvailable}kB"])

        return check_result
    
    except Exception as e:
        check_result = Check(status = Status.SKIP, message = f"Error reading /proc/meminfo: {e}", listOfChecks=[])
        print(f"Error reading /proc/meminfo: {e}")
        return check_result
