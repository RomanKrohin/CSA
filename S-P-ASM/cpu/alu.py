class ALU:
    
    def __init__(self):
        self.result = None
        
    def add (self ,first: int, second: int) -> None:
        self.result = first + second
        
    def sub (self ,first: int, second: int) -> None:
        self.result = first - second
        
    def mul (self ,first: int, second: int) -> None:
        self.result = first * second
        
    def div (self ,first: int, second: int) -> None:
        self.result = first // second
        