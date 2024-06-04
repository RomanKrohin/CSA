from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU
import logging

def add(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.add(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()


def sub(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.sub(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()

    
def div(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.div(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()

    
def mul(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.mul(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()
        
def push(self, arg: []):
    if (str(int(arg[2]))=="0"): 
        self.stack_memory.push((arg[1]))
        self.stack_inscrutions.pop()
    else:
        self.stack_memory.push((int(load_var(self, arg[1]))))
        self.stack_inscrutions.pop()
    

def pop(self, arg: []):
    self.stack_memory.pop()
    self.stack_inscrutions.pop()

    
def jmp(self, arg: []):
    self.stack_inscrutions.data.clear()
    self.stack_inscrutions.pop()
    self.command_pointer=int(arg[1])-1

        
def jeq(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.eq(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_inscrutions.pop()
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    
        
def jne(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.ne(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_inscrutions.pop()
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    
    
def jla(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.la(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_inscrutions.pop()
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    
    
def jle(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.ALU.le(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.ALU.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_inscrutions.pop()
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    
    
def load_int_to_var(self, arg: []):
    self.data_memory.write(arg[1], self.stack_memory.peek())
    self.stack_inscrutions.pop()
    self.stack_memory.pop()

    
def set_var(self, arg: []):
    self.data_memory.write(arg[1], arg[2])
    self.stack_inscrutions.pop()


    
def load_var(self, var_adr: str) -> str:
    return self.data_memory.read(var_adr)


def output(self, arg: []):
    self.output_device.append(chr(int(self.stack_memory.peek())))
    self.stack_memory.pop()
    self.stack_inscrutions.pop()

    
def input(self, arg: []):
    if len(self.input_device)==0:
        self.stack_memory.push(0)
    else:
        self.stack_memory.push((ord(self.input_device[0])))
        del self.input_device[0]
    self.stack_inscrutions.pop()


def incr(self, arg: []):
    self.ALU.add(int(self.stack_memory.peek()), 1)
    self.stack_memory.pop()
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()

    
def decr(self, arg: []):
    self.ALU.sub(int(self.stack_memory.peek()), 1)
    self.stack_memory.pop()
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()

    
def hlt(self, arg: []):
    self.stack_inscrutions.pop()
    print(self.output_device)
    print(self.data_memory.data)
    exit(0)
    
def mod(self, arg: []):
    self.ALU.mod(int(self.stack_memory.peek()), int(arg[1]))
    self.stack_memory.push((self.ALU.result))
    self.stack_inscrutions.pop()

def load_by_adr(self, arg: []):
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.data_memory.write(self.stack_memory.peek(), self.tmp.peek())
    self.tmp.pop()
    self.stack_inscrutions.pop()

def push_by_adr(self, arg: []):
    self.stack_memory.push(self.data_memory.read(self.stack_memory.peek()))
    self.stack_inscrutions.pop()
    
class Control_unit:
        
    def __init__(self) -> None:
        self.command_pointer: int = 0
        self.instruction_memory = None
        self.data_memory = None
        self.tmp=Stack()
        self.stack_memory = None
        self.stack_inscrutions = None
        self.output_device=[]
        self.input_device=['R', 'o', 'm', 'a', 'n']
        self.ALU = ALU()
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
                                instr_stack: Stack):
        self.data_memory=Memory()
        self.instruction_memory=insrt_mem
        self.stack_inscrutions=instr_stack
        self.stack_memory=data_stack
        self.inter_stack= Stack()
                        
        
    def process(self) -> None:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger('my_logger')
        while True:
            if self.stack_inscrutions.size()<1:
                self.stack_inscrutions.data = [ self.instruction_memory.data[self.command_pointer] ] + self.stack_inscrutions.data
            self.command_pointer+=1
            self.commands[self.stack_inscrutions.peek()[0]](self, self.stack_inscrutions.peek())
            logger.info(self.stack_memory.data)
            if (self.command_pointer>=len(self.instruction_memory.data)):
                self.stack_inscrutions.data = [ ['HLT', 0, 0] ] + self.stack_inscrutions.data
        
            