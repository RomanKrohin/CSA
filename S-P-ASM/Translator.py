def to_binary(machine_code: dict) -> bytes:
    binary_code = b""
    for label in machine_code.keys():
        block = b""
        block+= int(label, 16).to_bytes(1, "big")
        for instruction in  machine_code.get(label):
            block += int(instruction[0], 16).to_bytes(2,"big")
            block += int(instruction[1], 16).to_bytes(2,"big")
            block += int(instruction[2],16).to_bytes(2,"big")
            block += int(instruction[3],16).to_bytes(2,"big")
        block+=b"\0\0\0\0\0"
        binary_code+=block
    return binary_code

def from_binary(binary_code: bytes) -> dict:
    machine_code = {}
    i = 0
    while i < len(binary_code):
        label = int.from_bytes(binary_code[i:i+1], "big")
        i += 1
        instructions = []
        while i < len(binary_code) and binary_code[i:i+5] != b'\0\0\0\0\0':
            opcode = int.from_bytes(binary_code[i:i+2], "big")
            operand1 = int.from_bytes(binary_code[i+2:i+4], "big")
            operand2 = int.from_bytes(binary_code[i+4:i+6], "big")
            operand3 = int.from_bytes(binary_code[i+6:i+8], "big")
            instructions.append([hex(opcode), hex(operand1), hex(operand2), hex(operand3)])
            i += 8
        machine_code[hex(label)] = instructions
        i += 5
    return machine_code