from translate.Parser import run
from translate.Translator import to_binary, from_binary
from cpu.loader_to_cpu import load_binary_code

if __name__ == "__main__":
    load_binary_code(run("examples/Hello_user_name.SPASM"))