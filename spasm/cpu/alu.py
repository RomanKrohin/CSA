class ALU:
    
    def __init__(self):
        self.result = None
        self.zero= False
        self.neg= False
        self.logger = None
        
    def add (self ,first: int, second: int) -> None:
        self.result = first + second
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing ADD {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def sub (self ,first: int, second: int) -> None:
        self.result = first - second
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing SUB {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def mul (self ,first: int, second: int) -> None:
        self.result = first * second
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing MUL {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
    
    def mod (self ,first: int, second: int) -> None:
        self.result = first % second
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing MOD {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def div (self ,first: int, second: int) -> None:
        self.result = first // second
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing DIV {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def eq(self ,first: int, second: int) -> None:
        self.result = int(first==second)
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing COMPARE == {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def ne(self ,first: int, second: int) -> None:
        self.result = int(first!=second)
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing COMPARE != {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def la(self ,first: int, second: int) -> None:
        self.result = int(first>second)
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing COMPARE > {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def le(self ,first: int, second: int) -> None:
        self.result = int(first<second)
        self.zer = self.result==0
        self.neg = self.result < 0
        self.logger.info(f'Executing COMAPRE < {first} and {second} | {self.get_status()}', extra={'location': 'ALU'})
        
    def get_status(self) -> str:
        return f'ALU result={self.result} | zero={self.zero} | result={self.neg}'
        
        