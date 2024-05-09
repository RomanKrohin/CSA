class ALU:
    
    def __init__(self):
        self.result = None
        self.compare_symbol_to_lambda = {
            '0x3e8': lambda x, y: x>y,
            '0x7d0': lambda x, y: x==y,
            '0xbb8': lambda x, y: x<y   
        }
        
    def add (self ,first: int, second: int) -> None:
        self.result = first + second
        
    def sub (self ,first: int, second: int) -> None:
        self.result = first - second
        
    def mul (self ,first: int, second: int) -> None:
        self.result = first * second
        
    def div (self ,first: int, second: int) -> None:
        self.result = first // second
        
    def compare(self, first, second, code_of_symbol):
        self.result = int(self.compare_symbol_to_lambda[code_of_symbol](first, second))
        