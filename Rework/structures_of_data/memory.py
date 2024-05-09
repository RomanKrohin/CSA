class Memory:
    def __init__(self) -> None:
        self.data = {}

    def write(self, address: str, value):
        self.data[address] = value

    def read(self, address: str):
        return self.data.get(address, None)

    def read_string(self, address: str):
        result = ""
        while True:
            char = self.read(address)
            if char == '\0' or char is None:
                break
            result += char
            address = str(int(address, 16) + 1)
        return result
