from cpu.machine import Machine
from translate.parser import reset_globals, run


def start_work(file: str, in_file: str) -> None:
    machine = Machine()
    machine.configurate(run(file), in_file)
    reset_globals()
    machine.run()


if __name__ == "__main__":
    start_work("examples/prob1.SPASM", "../input/input.txt")
