class ALU:
    
    def __init__(self):
        self.result = None
        self.zero= False
        self.neg= False
        
    def add (self ,first: int, second: int) -> None:
        self.result = first + second
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def sub (self ,first: int, second: int) -> None:
        self.result = first - second
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def mul (self ,first: int, second: int) -> None:
        self.result = first * second
        self.zer = self.result==0
        self.neg = self.result < 0
    
    def mod (self ,first: int, second: int) -> None:
        self.result = first % second
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def div (self ,first: int, second: int) -> None:
        self.result = first // second
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def eq(self ,first: int, second: int) -> None:
        self.result = int(first==second)
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def ne(self ,first: int, second: int) -> None:
        self.result = int(first!=second)
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def la(self ,first: int, second: int) -> None:
        self.result = int(first>second)
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def le(self ,first: int, second: int) -> None:
        self.result = int(first<second)
        self.zer = self.result==0
        self.neg = self.result < 0
        
    def get_status(self) -> str:
        return f'ALU result={self.result} | zero={self.zero} | result={self.neg}'
        
        