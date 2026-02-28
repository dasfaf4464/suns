from enum import Enum, auto

class Position(Enum):
    PG = "PG"
    SG = "SG"
    G = "G"
    SF = "SF"
    PF = "PF"
    F = "F"
    C = "C"
    TEST = "TEST"

class Side(Enum):
    OFF = auto()
    DEF = auto()