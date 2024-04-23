from translate.Translator import from_binary
from cpu.control_unit import Control_unit
from structures_of_data.memory import Memory
from structures_of_data.stack import Stack

def load_binary_code (file: str):
    all_binary_code = b""
    with open (file, "rb") as f:
        all_binary_code += f.read()
    control_unit = Control_unit()
    instr_memory = Memory()
    instr_memory.data= from_binary(all_binary_code)
    control_unit.connect_data_structures(instr_memory, Stack(), Stack())
    control_unit.process()
    