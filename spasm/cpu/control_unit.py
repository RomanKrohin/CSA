
from structures_of_data.memory import Memory
from structures_of_data.stack import Stack

from cpu.alu import Alu
from cpu.input_device import InputDevice
from cpu.output_device import OutputDevice


def add(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.add(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push(self.Alu.result)
    return "Executing ADD"


def sub(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.sub(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push(self.Alu.result)
    return "Executing SUB"


def div(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.div(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push(self.Alu.result)
    return "Executing DIV"


def mul(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.mul(int(self.stack_memory.peek()), int(self.tmp.peek()))
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    self.stack_memory.push(self.Alu.result)
    return "Executing MUL"

def push(self, arg: []) -> str:
    if (str(int(arg[2]))=="0"):
        self.stack_memory.push(arg[1])
        return f"Executing PUSH VALUE #{arg[1]}"
    self.stack_memory.push(int(load_var(self, arg[1])))
    return f"Executing PUSH VALUE {arg[1]}"



def pop(self, arg: []) -> str:
    self.stack_memory.pop()
    return "Executing POP"


def jmp(self, arg: []):
    self.stack_inscrutions.data.clear()
    self.command_pointer=int(arg[1])-1
    return f"Executing JMP ADR {int(arg[1])}"


def jeq(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.eq(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.Alu.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f"Executing JEQ ADR {int(arg[1])}"


def jne(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.ne(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.Alu.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f"Executing JNE ADR {int(arg[1])}"


def jla(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.la(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.Alu.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f"Executing JLA ADR {int(arg[1])}"


def jle(self, arg: []) -> str:
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    self.Alu.le(int(self.stack_memory.peek()), int(self.tmp.peek()))
    if (self.Alu.result==1):
        self.stack_inscrutions.data.clear()
        self.command_pointer=int(arg[1])-1
    self.stack_memory.push(self.tmp.peek())
    self.tmp.pop()
    return f"Executing JLE ADR {int(arg[1])}"


def load_int_to_var(self, arg: []) -> str:
    self.data_memory.write(arg[1], self.stack_memory.peek())
    self.stack_memory.pop()
    return f"Executing LOAD ADR {int(arg[1])}"


def set_var(self, arg: []) -> str:
    self.data_memory.write(arg[1], arg[2])
    return f"Executing INIT ADR {int(arg[1])} VALUE {arg[2]}"



def load_var(self, var_adr: str):
    return self.data_memory.read(var_adr)


def output(self, arg: []) -> str:
    tmp = chr(int(self.stack_memory.peek()))
    self.output_device.add_symbol(chr(int(self.stack_memory.peek())))
    self.stack_memory.pop()
    return f"Executing PRINT VALUE {tmp}"


def print_symbol(self, arg: []) -> str:
    if len(self.input_device.input_array)==0:
        self.stack_memory.push(0)
        return f"Executing READ VALUE {0}"
    tmp = (ord(self.input_device.input_array[0]))
    self.stack_memory.push(ord(self.input_device.input_array[0]))
    self.input_device.input_array = self.input_device.input_array[1:]
    return f"Executing READ VALUE {tmp}"



def incr(self, arg: []) -> str:
    self.Alu.add(int(self.stack_memory.peek()), 1)
    self.stack_memory.pop()
    self.stack_memory.push(self.Alu.result)
    return "Executing INCR"


def decr(self, arg: []) -> str:
    self.Alu.sub(int(self.stack_memory.peek()), 1)
    self.stack_memory.pop()
    self.stack_memory.push(self.Alu.result)
    return "Executing DECR"


def hlt(self, arg: []) -> str:
    self.halted = True
    return "Executing HLT"


def mod(self, arg: []) -> str:
    self.Alu.mod(int(self.stack_memory.peek()), int(arg[1]))
    self.stack_memory.push(self.Alu.result)
    return f"Executing MOD VALUE {int(arg[1])}"

def load_by_adr(self, arg: []) -> str:
    tmp1 = self.stack_memory.peek()
    self.tmp.push(self.stack_memory.peek())
    self.stack_memory.pop()
    tmp2 = self.stack_memory.peek()
    self.data_memory.write(self.stack_memory.peek(), self.tmp.peek())
    self.tmp.pop()
    return f"Executing LADR ADR {tmp2} VALUE {tmp1}"

def push_by_adr(self, arg: []) -> str:
    tmp = self.stack_memory.peek()
    self.stack_memory.push(self.data_memory.read(self.stack_memory.peek()))
    return f"Executing PADR ADR {tmp}"

class ControlUnit:

    def __init__(self) -> None:
        self.command_pointer: int = 0
        self.instruction_memory = None
        self.data_memory = None
        self.tmp=Stack()
        self.stack_memory = None
        self.input_device = None
        self.output_device = None
        self.Alu = None
        self.halted=False
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
            "READ": print_symbol,
            "PADR": push_by_adr,
            "LADR": load_by_adr,
            "MOD": mod,
            "ADR": push}

    def connect_data_structures(self, insrt_mem: Memory,
                                data_stack: Stack,
                                instr_stack: Stack,
                                Alu: Alu,
                                input_device: InputDevice(),
                                output_device: OutputDevice(),
                                logger):
        self.data_memory=Memory()
        self.instruction_memory=insrt_mem
        self.stack_inscrutions=instr_stack
        self.stack_memory=data_stack
        self.inter_stack= Stack()
        self.output_device = output_device
        self.input_device = input_device
        self.Alu = Alu
        self.logger = logger


    def process(self) -> None:
            self.logger.info(f"Count of instructions {self.counter_instr} | Command pointer {self.command_pointer} ", extra={"location": "CONTROL UNIT"})
            while not self.halted:
                command = self.instruction_memory.data[self.command_pointer]
                self.command_pointer += 1
                self.logger.info(self.commands[command[0]](self, command), extra={"location": "INCRUCTIONS"})
                self.counter_instr += 1
                self.logger.info(self.stack_memory.data, extra={"location": "STACK MEMORY"})
                self.logger.info(f"Count of instructions {self.counter_instr} | Command pointer {self.command_pointer} ", extra={"location": "CONTROL UNIT"})
                if self.command_pointer >= len(self.instruction_memory.data):
                    self.stack_inscrutions.data = [["HLT", 0, 0], *self.stack_inscrutions.data]

