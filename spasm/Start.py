from translate.Parser import run
from cpu.machine import Machine

if __name__ == "__main__":
    machine = Machine()
    machine.configurate(run("examples/prob1.SPASM"))
    machine.run()