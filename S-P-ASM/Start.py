from Parser import run
from Translator import to_binary, from_binary

if __name__ == "__main__":
    print(from_binary (to_binary(run("test.SPASM"))))