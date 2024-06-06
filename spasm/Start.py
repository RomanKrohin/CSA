from cpu.machine import Machine
from translate.parser import run


def start_work(file: str, in_file: str) -> None:
    machine = Machine()
    machine.configurate(run(file), in_file)
    machine.run()


if __name__ == "__main__":
    start_work("examples/Input_test.SPASM", "../input/input.txt")
