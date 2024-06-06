class Stack:

    def __init__(self) -> None:
        self.data: list =[]

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self)

    def push(self, item: str):
        assert not self.size()>256, "Stack overflow"
        self.data.append(item)

    def pop(self):
        if (len(self.data)>0):
            del self.data[-1]

    def peek(self) -> str:
        return self.data[-1]

    def size(self) -> int:
        return len(self.data)
