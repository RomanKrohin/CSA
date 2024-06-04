from translate.Parser import run
from cpu.machine import Machine

if __name__ == "__main__":
    machine = Machine()
    machine.configurate(run("examples/Hello_user_name.SPASM"))
    machine.run()