from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU
from cpu.input_device import Input_device
from cpu.output_device import Output_device
import logging

def add(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.add(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    return f'Executing ADD'


def sub(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.sub(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    return f'Executing SUB'

    
def div(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.div(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    return f'Executing DIV'

    
def mul(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.mul(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    return f'Executing MUL'
        
def push(self, arg: []) -> str:
    if (str(int(arg[2]))=="0"): 
        self.stack_memory.push((arg[1]))
        return f'Executing PUSH VALUE #{arg[1]}'
    else:
        self.stack_memory.push((int(load_var(self, arg[1]))))
        return f'Executing PUSH VALUE {arg[1]}'    

    

def pop(self, arg: []) -> str:
    self.stack_memory.pop()
    return f'Executing POP'

    
def jmp(self, arg: []):
    self.stack_inscrutions.data.clear()
    self.command_pointer=int(arg[1])-1
    return f'Executing JMP ADR {int(arg[1])}'

        
def jeq(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.eq(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f'Executing JEQ ADR {int(arg[1])}'
    
        
def jne(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.ne(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f'Executing JNE ADR {int(arg[1])}'
    
    
def jla(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.la(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f'Executing JLA ADR {int(arg[1])}'
    
    
def jle(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.le(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f'Executing JLE ADR {int(arg[1])}'
    
    
def load_int_to_var(self, arg: []) -> str:
    self.data_memory.write(arg[1], self.stack_memory.peek())
    self.stack_memory.pop()
    return f'Executing LOAD ADR {int(arg[1])}'

    
def set_var(self, arg: []) -> str:
    self.data_memory.write(arg[1], arg[2])
    return f'Executing INIT ADR {int(arg[1])} VALUE {arg[2]}'


    
def load_var(self, var_adr: str):
    return self.data_memory.read(var_adr)


def output(self, arg: []) -> str:
    tmp = chr(int(self.stack_memory.peek()))
    self.output_device.add_symbol(chr(int(self.stack_memory.peek())))
    self.stack_memory.pop()
    return f'Executing PRINT VALUE {tmp}'

    
def input(self, arg: []) -> str:
    if len(self.input_device.input_array)==0:
        self.stack_memory.push(0)
        return f'Executing READ VALUE {0}'
    else:
        tmp = (ord(self.input_device.input_array[0]))
        self.stack_memory.push((ord(self.input_device.input_array[0])))
        self.input_device.input_array = self.input_device.input_array[1:]
        return f'Executing READ VALUE {tmp}'


def incr(self, arg: []) -> str:
    self.ALU.add(int(self.stack_memory.peek()), 1)
    self.stack_memory.pop()
    self.stack_memory.push((self.ALU.result))
    return f'Executing INCR'

    
def decr(self, arg: []) -> str:
    self.ALU.sub(int(self.stack_memory.peek()), 1)
    self.stack_memory.pop()
    self.stack_memory.push((self.ALU.result))
    return f'Executing DECR'

    
def hlt(self, arg: []) -> str:
    print(self.output_device.output_array)
    print(self.data_memory.data)
    self.logger.info('Executing HLT', extra={'location': 'INCRUCTIONS'})
    self.counter_instr+=1
    self.logger.info(f'Count of instructions {self.counter_instr}', extra={'location': 'CONTROL UNIT'})
    exit(0)
    
def mod(self, arg: []) -> str:
    self.ALU.mod(int(self.stack_memory.peek()), int(arg[1]))
    self.stack_memory.push((self.ALU.result))
    return f'Executing MOD VALUE {int(arg[1])}'

def load_by_adr(self, arg: []) -> str:
    tmp1 = self.stack_memory.peek()
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    tmp2 = self.stack_memory.peek()
    self.data_memory.write(self.stack_memory.peek(), self.tmp.peek())
    self.tmp.pop()
    return f'Executing LADR ADR {tmp2} VALUE {tmp1}'

def push_by_adr(self, arg: []) -> str:
    tmp = self.stack_memory.peek()
    self.stack_memory.push(self.data_memory.read(self.stack_memory.peek()))
    return f'Executing PADR ADR {tmp}'
    
class Control_unit:
        
    def __init__(self) -> None:
        self.command_pointer: int = 0
        self.instruction_memory = None
        self.data_memory = None
        self.tmp=Stack()
        self.stack_memory = None
        self.input_device = None
        self.output_device = None
        self.ALU = None
        self.logger = None
        self.counter_instr = 0
        self.commands = {
            "ADD": add,
            "HLT": hlt,
            "SUB": sub,
            "DIV": div,
            "MUL": mul, 
            "POP": pop, 
            "PUSH": push,
            "JMP": jmp,
            "JEQ": jeq,
            "JNE": jne,
            "JLA": jla,
            "JLE": jle,
            "INIT": set_var,
            "LOAD": load_int_to_var,
            "PRINT": output,
            "INCR": incr,
            "DECR": decr,
            "READ": input,
            "PADR": push_by_adr,
            "LADR": load_by_adr,
            "MOD": mod,
            "ADR": push}
        
    def connect_data_structures(self, insrt_mem: Memory, 
                                data_stack: Stack, 
                                instr_stack: Stack,
                                ALU: ALU,
                                input_device: Input_device(),
                                output_device: Output_device(),
                                logger):
        self.data_memory=Memory()
        self.instruction_memory=insrt_mem
        self.stack_inscrutions=instr_stack
        self.stack_memory=data_stack
        self.inter_stack= Stack()
        self.output_device = output_device
        self.input_device = input_device
        self.ALU = ALU
        self.logger = logger
                        
        
    def process(self) -> None:
        self.logger.info(f'Count of instructions {self.counter_instr} | Command pointer {self.command_pointer} ', extra={'location': 'CONTROL UNIT'})
        while True:
            command = self.instruction_memory.data[self.command_pointer]
            self.command_pointer+=1
            self.logger.info(self.commands[command[0]](self, command), extra={'location': 'INCRUCTIONS'})
            self.counter_instr+=1
            self.logger.info(self.stack_memory.data, extra={'location': 'STACK MEMORY'})
            self.logger.info(f'Count of instructions {self.counter_instr} | Command pointer {self.command_pointer} ', extra={'location': 'CONTROL UNIT'})
            if (self.command_pointer>=len(self.instruction_memory.data)):
                self.stack_inscrutions.data = [ ['HLT', 0, 0] ] + self.stack_inscrutions.data
        
            