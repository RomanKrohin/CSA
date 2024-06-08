class Memory:
    def __init__(self) -> None:
        self.data = {}

    def write(self, address: str, value):
        assert len(self.data) < 2**11, "Memory overflow"
        self.data[address] = value

    def read(self, address: str):
        return self.data.get(address, None)
