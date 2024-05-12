class Memory:
    def __init__(self) -> None:
        self.data = {}

    def write(self, address: str, value, type: str):
        self.data[address] = value
        if (type=='0x3'):
            self.data[hex(int(address,16)+1)] = '0x3'

    def read(self, address: str):
        return self.data.get(address, None)