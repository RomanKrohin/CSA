from translate.Parser import run
from translate.Translator import to_binary, from_binary
from cpu.loader_to_cpu import load_binary_code

if __name__ == "__main__":
    to_binary (run("examples/prob1.SPASM"), "output/test.bin")
    load_binary_code("output/test.bin")