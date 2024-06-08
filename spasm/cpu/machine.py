import logging
from datetime import datetime

from structures_of_data.memory import Memory
from structures_of_data.stack import Stack

from cpu.alu import Alu
from cpu.control_unit import ControlUnit
from cpu.input_device import InputDevice
from cpu.output_device import OutputDevice


class Machine:

    def __init__(self):
        self.CU = ControlUnit()
        self.input_device = InputDevice()
        self.output_device = OutputDevice()
        self.logger = logging.getLogger("control_unit_logger")
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(f"log/{datetime.now()}.log")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter("%(name)s - %(levelname)s - %(location)s - %(message)s")
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def configurate(self, machine_code: [], in_file: str):
        instr_memory = Memory()
        instr_memory.data= machine_code
        self.logger.info(machine_code, extra={"location": "INSTRUCTION MEMORY"})
        input_device = InputDevice()
        output_device = OutputDevice()
        input_device.conf(in_file)
        a = Alu()
        a.logger = self.logger
        self.CU.connect_data_structures(instr_memory, Stack(), Stack(), a, input_device, output_device, self.logger)

    def run(self):
        self.CU.process()
        self.CU.instruction_memory=[]
