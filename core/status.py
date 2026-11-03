from enum import IntFlag

class Status(IntFlag):
    OK = 0 # (000000)
    LOW = 3 # (000011)
    MED = 5 # (000101)
    HIGH = 9 # (001001)
    CRIT = 33 # (100001)
    SKIP = 16 # (010000)