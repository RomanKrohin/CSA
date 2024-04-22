class Stack:
    
    def __init__(self) -> None:
        self.data: list =[]
        
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return str(self)
    
    def push(self, item: str):
        self.data.append(item)
        
    def pop(self, item: str):
        del self.data[-1]
        
    def peek(self) -> str:
        return self.data[-1]
    
    def size(self) -> int:
        return len(self.data)