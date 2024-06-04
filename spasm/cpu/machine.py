from cpu.control_unit import Control_unit
from structures_of_data.memory import Memory
from structures_of_data.stack import Stack
from cpu.alu import ALU
from cpu.input_device import Input_device
from cpu.output_device import Output_device
import logging
from datetime import datetime

class Machine:
    
    def __init__(self):
        self.CU = Control_unit()
        self.input_device = Input_device()
        self.output_device = Output_device()
        self.logger = logging.getLogger('control_unit_logger')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(f'../log/{datetime.now()}.log')
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(location)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
    def configurate(self, machine_code: []):
        instr_memory = Memory()
        instr_memory.data= machine_code
        self.logger.info(machine_code, extra={'location': 'INSTRUCTION MEMORY'})
        input_device = Input_device()
        output_device = Output_device()
        input_device.conf("../input/input.txt")
        alu = ALU()
        alu.logger = self.logger
        self.CU.connect_data_structures(instr_memory, Stack(), Stack(), alu, input_device, output_device, self.logger)
    
    def run(self):
        self.CU.process()
        