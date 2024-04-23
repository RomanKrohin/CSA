from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU

def add(self, arg: []):
    self.ALU.add(int(self.stack_memory.peek()), int(arg[1], 16))
    self.stack_memory.pop()
    self.stack_memory.push(str(self.ALU.result))
    self.stack_inscrutions.pop()
        
def push(self, arg: []):
    print(str(int(arg[1], 16)))
    self.stack_memory.push(str(int(arg[1], 16))) 
    self.stack_inscrutions.pop()

def pop(self, arg: []):
    self.stack_memory.pop()
    self.stack_inscrutions.pop()
    
def jmp(self, arg: []):
    self.stack_inscrutions.data.clear()
    self.stack_inscrutions.pop()
    for _ in self.instruction_memory.data[arg[1]]:
            self.stack_inscrutions.data = [ _ ] + self.stack_inscrutions.data
    
def jif(self, arg: []):
    self.ALU.compare(int(self.stack_memory.peek()), int(arg[2], 16), arg[1])
    if self.ALU.result==1:
        self.stack_inscrutions.data.clear()
        self.stack_inscrutions.pop()
        for _ in self.instruction_memory.data[arg[3]]:
                self.stack_inscrutions.data = [ _ ] + self.stack_inscrutions.data
    else:
        self.stack_inscrutions.pop()

def set_var(self, arg: []):
    self.data_memory[int(arg[1], 16)-20] = arg[2] 
    self.stack_inscrutions.pop()
    
    
class Control_unit:
             
        
    def __init__(self) -> None:
        self.instruction_memory = None
        self.data_memory = None
        self.stack_memory = None
        self.stack_inscrutions = None
        self.ALU = ALU()
        self.commands = {
        "0x64": add, 
        "0xc8": pop, 
        "0x12c": push, 
        "0x190": jif, 
        "0x2bc": jmp,
        "0x420": set_var}
        
    def connect_data_structures(self, insrt_mem: Memory, 
                                data_stack: Stack, 
                                instr_stack: Stack):
        self.data_memory=["0"]*1000
        self.instruction_memory=insrt_mem
        self.stack_inscrutions=instr_stack
        self.stack_memory=data_stack
        
    def process(self) -> None:
        for _ in self.instruction_memory.data['0x1']:
            self.stack_inscrutions.data = [ _ ] + self.stack_inscrutions.data
        
        while self.stack_inscrutions.size()>0:
            self.commands[self.stack_inscrutions.peek()[0]](self, self.stack_inscrutions.peek())
        print(self.stack_memory.data)
        print(self.data_memory)