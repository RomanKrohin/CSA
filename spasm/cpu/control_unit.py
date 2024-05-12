from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU
import logging
from cpu.interruption import Interruption
from cpu.interruption import InterruptionType
from IOmanagers.output_manager import Output_manager


def add(self, arg: []):
    self.ALU.add(int(self.stack_memory.peek(), 16), int(arg[1], 16))
    self.do_tick()
    self.stack_memory.pop()
    self.do_tick()
    self.stack_memory.push(hex(self.ALU.result))
    self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()
        
def push(self, arg: []):
    print(321)
    if (str(int(arg[2], 16))=="0"): 
        self.stack_memory.push((arg[1]))
        self.do_tick() 
        self.stack_inscrutions.pop()
        self.do_tick()
    else:
        self.stack_memory.push(hex(int(load_var(self, arg[1]), 16)))
        self.do_tick() 
        self.stack_inscrutions.pop()
        self.do_tick()
    self.do_tick()


def pop(self, arg: []):
    self.stack_memory.pop()
    self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()
    
def jmp(self, arg: []):
    self.stack_inscrutions.data.clear()
    self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()
    self.command_pointer=int(arg[1], 16)-1
    self.do_tick()
        
def load_int_to_var(self, arg: []):
    self.data_memory.write(arg[1], self.stack_memory.peek(), '0x3')
    self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()
    self.stack_memory.pop()
    self.do_tick()
    
def set_var(self, arg: []):
    self.data_memory.write(arg[1], arg[2], arg[3])
    self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()

    
def load_var(self, var_adr: str) -> str:
    self.do_tick()
    return self.data_memory.read(var_adr)


def output(self, arg: []):
    self.inter_stack.push(Interruption(InterruptionType.OUTPUT))
    self.do_tick()
    count=0
    self.stack_memory.push('\0')
    self.do_tick()
    if (self.data_memory.data[hex(int(arg[1],16)+1)]=='0x3'):
            self.stack_memory.push(self.data_memory.data[hex(int(arg[1],16))])
            self.do_tick()
            self.stack_memory.push('0x2')
            self.do_tick()
    
    else:    
        while(count<40 and self.data_memory.data[hex(int(arg[1],16)+count)]!='0x0'):
            self.stack_memory.push(self.data_memory.data[hex(int(arg[1],16)+count)])
            self.do_tick()
            count+=1
        self.stack_memory.push('0x1')
        self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()
    
def input(self, arg: []):
    print(123)
    self.inter_stack.push(Interruption(InterruptionType.INPUT))
    self.do_tick()
    self.in_adress=arg[1]
    self.do_tick()
    self.stack_inscrutions.pop()
    self.do_tick()
    
class Control_unit:
        
    def __init__(self) -> None:
        self.time: int = 0
        self.command_pointer: int = 0
        self.instruction_memory = None
        self.input_stack= Stack()
        self.data_memory = None
        self.in_adress=None
        self.stack_memory = None
        self.stack_inscrutions = None
        self.input_device={5: 'p', 10: 'i', 15: 'v', 20: 'o', 25: '\0'}
        self.ALU = ALU()
        self.commands = {
            "0x64": add, 
            "0xc8": pop, 
            "0x12c": push,
            "0x2bc": jmp,
            "0x420": set_var,
            "0x520": load_int_to_var,
            "0x290": output,
            "0x390": input}
        
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
            self.do_tick()
    
            match interruption.inter_type:
                case InterruptionType.OUTPUT:
                    self.inter_stack.pop()
                    self.do_tick()
                    value=""
                    type_flag=self.stack_memory.peek()
                    self.do_tick()
                    self.stack_memory.pop()
                    self.do_tick()
                    while(self.stack_memory.peek()!='\x00'):
                        if (type_flag=='0x1'):
                            value+=chr(int(self.stack_memory.peek(), 16))
                            self.do_tick()
                        self.do_tick()
                        if (type_flag=='0x2'):
                            value+=str(int(self.stack_memory.peek(), 16))
                            self.do_tick()
                        self.do_tick()
                        self.stack_memory.pop()
                    self.do_tick()
                    self.stack_memory.pop()
                    self.do_tick()
                    value = value[::-1]
                    om = Output_manager()
                    om.set_result_filepath("output.txt")
                    om.write(value)
                case InterruptionType.INPUT:
                    tmp =[]
                    for key in self.input_device.keys():
                        if self.time>key:
                            tmp.append(key)
                            self.input_stack.push(self.input_device[key])
                    for i in tmp:
                        del self.input_device[i]
                    if self.input_stack.peek()=='\x00':
                        self.inter_stack.pop()
                        self.do_tick()
                        for i in range(0,self.input_stack.size()):
                            self.data_memory.data[hex(int(self.in_adress,16)+i)]=str(hex(ord(self.input_stack.data[0])))
                            self.input_stack.data=self.input_stack.data[1:]
                            
                    print(self.data_memory.data)
                        
        
    def process(self) -> None:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger('my_logger')
        while True:
            print(self.instruction_memory.data[self.command_pointer])
            self.stack_inscrutions.data = [ self.instruction_memory.data[self.command_pointer] ] + self.stack_inscrutions.data
            self.do_tick()
            self.command_pointer+=1
            self.do_tick()            
            self.commands[self.stack_inscrutions.peek()[0]](self, self.stack_inscrutions.peek())
            self.do_tick()
            self.init_interuption()
            logger.info(self.stack_memory.data)
            if (self.command_pointer>=len(self.instruction_memory.data)):
                exit(0)
            self.do_tick()
            