from translate.Translator import from_binary

def load_binary_code (file: str):
    all_binary_code = b""
    with open (file, "rb") as f:
        all_binary_code += f.read()
    print(from_binary(all_binary_code))
    