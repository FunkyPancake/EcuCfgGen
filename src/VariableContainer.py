class VariableContainer:
    def __init__(self, a, b, c):
        self.entry = "Measurement" if a is True else "Calibration"
        self.entry_type = None
        self.name = b
        self.var_type = c
        self.value =0
        self.format = ""
        self.description = 0
        self.address = 0
        self.size = 0
        self.axis_ref = None
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c
