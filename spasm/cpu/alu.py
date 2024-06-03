class ALU:
    
    def __init__(self):
        self.result = None
        
    def add (self ,first: int, second: int) -> None:
        self.result = first + second
        
    def sub (self ,first: int, second: int) -> None:
        self.result = first - second
        
    def mul (self ,first: int, second: int) -> None:
        self.result = first * second
    
    def mod (self ,first: int, second: int) -> None:
        self.result = first % second
        
    def div (self ,first: int, second: int) -> None:
        self.result = first // second
        
    def eq(self ,first: int, second: int) -> None:
        self.result = int(first==second)
        
    def ne(self ,first: int, second: int) -> None:
        self.result = int(first!=second)
        
    def la(self ,first: int, second: int) -> None:
        self.result = int(first>second)
        
    def le(self ,first: int, second: int) -> None:
        self.result = int(first<second)
        
        