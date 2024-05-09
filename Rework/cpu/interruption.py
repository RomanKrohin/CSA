from enum import Enum

class InterruptionType(Enum):
    INPUT = 0
    OUTPUT = 1
    STOP = 2
    ERROR = 3 
    
class Interruption:
    def __init__(self, inter_type: InterruptionType) -> None:
        self.inter_type = inter_type