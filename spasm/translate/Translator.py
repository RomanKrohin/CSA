def to_binary(machine_code: dict, file: str) -> bytes:
    binary_code = b""
    for instruction in  machine_code:
        block = b""
        block += int(instruction[0], 16).to_bytes(2,"big")
        block += int(instruction[1], 16).to_bytes(2,"big")
        block += int(instruction[2],16).to_bytes(2,"big")
        block += int(instruction[3],16).to_bytes(2,"big")
        binary_code+=block
    with open(file, "wb") as f:
        f.write(binary_code)
    return binary_code

def from_binary(binary_code: bytes) -> dict:
    i = 0
    while i < len(binary_code):
        instructions = []
        while i < len(binary_code):
            opcode = int.from_bytes(binary_code[i:i+2], "big")
            operand1 = int.from_bytes(binary_code[i+2:i+4], "big")
            operand2 = int.from_bytes(binary_code[i+4:i+6], "big")
            operand3 = int.from_bytes(binary_code[i+6:i+8], "big")
            instructions.append([hex(opcode), hex(operand1), hex(operand2), hex(operand3)])
            i += 8
    return instructions