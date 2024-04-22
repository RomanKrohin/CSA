class Memory:
    
    def __init__(self) -> None:
        self.data : dict = None
        
    def set_memory(self, items: dict):
        self.data = items
        
    def set_cell(self, adress: str, item: str):
        if (adress not in self.data.keys()):
            self.data.put(adress, item)
            
    def get_cell (self, adress : str) -> str:
        return self.data.get(adress)
        
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return str(self)