from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU
import logging
from cpu.interruption import Interruption
from cpu.interruption import InterruptionType
from IOmanagers.output_manager import Output_manager


def add(self, arg: []):
    self.ALU.add(int(self.stack_memory.peek(), 16), int(arg[1], 16))
    self.stack_memory.pop()
    self.stack_memory.push(hex(self.ALU.result))
    self.stack_inscrutions.pop()
        
def push(self, arg: []):
    if (str(int(arg[2], 16))=="0"): 
        self.stack_memory.push((arg[1])) 

        self.stack_inscrutions.pop()

    else:
        self.stack_memory.push(str(int(load_var(self, arg[1]), 16))) 

        self.stack_inscrutions.pop()


def pop(self, arg: []):
    self.stack_memory.pop()
    self.stack_inscrutions.pop()
    
def jmp(self, arg: []):
    self.stack_inscrutions.data.clear()
    self.stack_inscrutions.pop()
    self.command_pointer=int(arg[1], 16)-1
    self.label_pointer: str = arg[1]

    
def jif(self, arg: []):
    self.ALU.compare(int(self.stack_memory.peek()), int(arg[2], 16), arg[1])
    if self.ALU.result==1:
        self.stack_inscrutions.data.clear()

        self.stack_inscrutions.pop()

        self.command_pointer=0

        self.label_pointer: str = arg[3]

    else:
        self.stack_inscrutions.pop()

        
def load_int_to_var(self, arg: []):
    self.data_memory.write(arg[1], self.stack_memory.peek(), '0x3')
    self.stack_inscrutions.pop()
    self.stack_memory.pop()
    
def set_var(self, arg: []):
    self.data_memory.write(arg[1], arg[2], arg[3])
    self.stack_inscrutions.pop()

    
def load_var(self, var_adr: str) -> str:
    return self.data_memory.read(var_adr)


def output(self, arg: []):
    self.inter_stack.push(Interruption(InterruptionType.OUTPUT))
    count=0
    self.stack_memory.push('\0')
    if (self.data_memory.data[hex(int(arg[1],16)+1)]=='0x3'):
            self.stack_memory.push(self.data_memory.data[hex(int(arg[1],16))])
    
            self.stack_memory.push('0x2')
    
    else:    
        while(count<40 and self.data_memory.data[hex(int(arg[1],16)+count)]!='0x0'):
            self.stack_memory.push(self.data_memory.data[hex(int(arg[1],16)+count)])
    
            count+=1
    

        self.stack_memory.push('0x1')

    self.stack_inscrutions.pop()
    
    
class Control_unit:
        
    def __init__(self) -> None:
        self.time: int = 0
        self.label_pointer: str = '0x1'
        self.command_pointer: int = 0
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
            "0x420": set_var,
            "0x520": load_int_to_var,
            "0x290": output}
        
    def do_tick(self):
        self.time+=1
    
    def connect_data_structures(self, insrt_mem: Memory, 
                                data_stack: Stack, 
                                instr_stack: Stack):
        self.data_memory=Memory()
        self.instruction_memory=insrt_mem
        self.stack_inscrutions=instr_stack
        self.stack_memory=data_stack
        self.inter_stack= Stack()
        
    def init_interuption(self) -> None:
        while self.inter_stack.size()>0:
            interruption: Interruption = self.inter_stack.peek()
    
            self.inter_stack.pop()
    
            match interruption.inter_type:
                case InterruptionType.OUTPUT:
                    value=""
                    type_flag=self.stack_memory.peek()
                    self.stack_memory.pop()
                    while(self.stack_memory.peek()!='\x00'):
                        if (type_flag=='0x1'):
                            value+=chr(int(self.stack_memory.peek(), 16))
                        if (type_flag=='0x2'):
                            value+=str(int(self.stack_memory.peek(), 16))
                
                        self.stack_memory.pop()
                
                    self.stack_memory.pop()
            
                    value = value[::-1]
                    om = Output_manager()
                    om.set_result_filepath("output.txt")
                    om.write(value)
                case InterruptionType.INPUT:
                    print(13323)
        
    def process(self) -> None:
                
        print(self.instruction_memory.data)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger('my_logger')
        while True:
            self.stack_inscrutions.data = [ self.instruction_memory.data[self.command_pointer] ] + self.stack_inscrutions.data
            self.command_pointer+=1            
            self.commands[self.stack_inscrutions.peek()[0]](self, self.stack_inscrutions.peek())
            self.init_interuption()
            print(self.command_pointer)
            if (self.command_pointer>len(self.instruction_memory.data)):
                print(123)
                exit(0)
            logger.info(self.stack_memory.data)
