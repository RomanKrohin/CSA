class InputDevice:

    def __init__(self):
        self.input_array=[]

    def conf(self, file: str):
        with open(file, encoding="utf-8") as f:
            content = f.read()

        self.input_array = list(content)
