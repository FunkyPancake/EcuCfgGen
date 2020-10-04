class Characteristic:
    def __init__(self,lines):
        pass
class Measurement:
    def __init__(self):
        self.name -""
        self.description=""
        self.data_type=""
        self.conversion="debug_no_conversion"
        self.resolution=""
        self.accuracy=""
        self.lower_limit=""
        self.upper_limit=""
        self.ecu_address=""

    def __init__(self,lines):

        self.name = lines[0]
        self.description=lines[1]
        self.data_type=lines[2]
        self.conversion=lines[3]
        self.resolution=lines[4]
        self.accuracy=lines[5]
        self.lower_limit=lines[6]
        self.upper_limit=lines[7]
        self.ecu_address=lines[8]

    def update_adr(self,adr):
        self.ecu_address = f'0x{adr}'

class VariableContainer:
    def __init__(self, a, b, c):
        self.entry = "Measurement" if a is True else "Calibration"
        if self.entry == "Calibration":
            self.entry_type = None
            self.value = 0
            self.axis_ref = None
        else:
            self.entry_type = None
            self.value = 0
            self.axis_ref = None
        self.name = b
        self.var_type = c
        self.format = ""
        self.description = ""
        self.address = 0
        self.byte_size = None

    def __eq__(self, other):
        return self.name == other.name and self.entry == other.entry and self.var_type == other.var_type

class A2LContainer:
    def __init__(self):
        self.prefix = []
        self.measurement = []
        self.calibration = []