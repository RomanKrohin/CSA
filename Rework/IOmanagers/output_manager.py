
class Output_manager:
    def __init__(self) -> None:
        self.output_device = None
        
    def set_result_filepath(self, result_filepath):
        try:
            self.output_device = open(result_filepath, 'w')
        except FileNotFoundError:
            exit(1)

    def write(self, data):
        self.output_device.write(data)
        self.output_device.flush()

    def turn_off(self):
    
        self.output_device.close()

    def str(self):
        return "OutputManager"

    def repr(self):
        return str(self)
    