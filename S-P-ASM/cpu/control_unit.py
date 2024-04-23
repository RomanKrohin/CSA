from structures_of_data.memory import Memory
from structures_of_data.stack import Stack

class Control_unit:
    
    commands = {
        
    }
    
    def __init__(self) -> None:
        self.instruction_memory = None
        self.data_memory = None
        self.stack_memory = None
        self.stack_inscrutions = None
        
    def connect_data_structures(self, insrt_mem: Memory, 
                                data_mem: Memory, 
                                data_stack: Stack, 
                                instr_stack: Stack):
        self.data_memory=data_mem
        self.instruction_memory=insrt_mem
        self.stack_inscrutions=instr_stack
        self.stack_memory=data_stack
        
        def process(self):
            return None