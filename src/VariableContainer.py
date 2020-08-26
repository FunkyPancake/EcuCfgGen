from lxml import etree


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

    def serialize(self):
        entry = etree.Element('Entry')

        name = etree.SubElement(entry, "NAME")
        name.text = self.name

        ecu_address = etree.SubElement(entry, "ECU_ADDRESS")
        ecu_address.text = hex(self.address)

        desc = etree.SubElement(entry, "DESCRIPTION")
        desc.text = self.description
        # var_type
        # scaling
        # lim_min
        # lim_max
        # format
        # if(self.entry == "Calibation"):
        #     entry_type = etree.SubElement(entry,"")

        return entry
