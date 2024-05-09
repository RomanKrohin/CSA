class InputManager:
    def __init__(self):
        self._input = None
        self.input_device = None
        self.logger = None

    def set_input_device(self, input_device: str):
        try:
            self.input_device = open(input_device, 'r')
            temp = []
            for line in self.input_device.readlines():
                time, value = line.strip().split(":")
                temp.append((int(time), value if value != "" else " "))

            self.set_input(temp)
        except FileNotFoundError:
            exit(1)

    def get_input(self):
        return self._input

    def set_input(self, arg):
        self._input = arg

    def turn_off(self):
        if self.input_device is not None:
            self.input_device.close()

    def __str__(self):
        return "InputManager"

    def __repr__(self):
        return str(self)
