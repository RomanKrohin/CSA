from cpu.control_unit import Control_unit
from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU
from cpu.input_device import Input_device
from cpu.output_device import Output_device
import logging

class Machine:
    
    def __init__(self):
        self.CU = Control_unit()
        self.input_device = Input_device()
        self.output_device = Output_device()
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger('my_logger')
        
    def configurate(self, machine_code: []):
        instr_memory = Memory()
        instr_memory.data= machine_code
        input_device = Input_device()
        output_device = Output_device()
        input_device.conf("../input/input.txt")
        self.CU.connect_data_structures(instr_memory, Stack(), Stack(), ALU(), input_device, output_device, self.logger)
    
    def run(self):
        self.CU.process()
        