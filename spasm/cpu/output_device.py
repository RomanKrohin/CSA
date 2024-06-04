class Output_device:
    
    def __init__(self):
        self.output_array=[]
        
    def add_symbol(self, c: chr):
        self.output_array.append(c)
        
    def print(self) -> str:
        str = ""
        for c in self.output_array:
            str+=c
        return str