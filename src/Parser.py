import os
from src.VariableContainer import VariableContainer


class Parser:
    def __init__(self):
        self.file_list = []

    @staticmethod
    def list_files(root_path, extension):
        file_list = []
        for root, dirs, files in os.walk(root_path):
            [file_list.append(f"{root.split(root_path)[1]}/{file}".replace("\\", "/")) for file in files if
             extension in file]
        return file_list

    def parse_c_file(self, file_path):
        variable_list = []
        fd = open(file_path, "r")
        for line in fd.readlines():
            if "START_SEC" in line:
                is_cal_sec = "CAL" in line
                section_open = True
                continue
            if "STOP_SEC" in line:
                section_open = False
                continue
            if "#include" in line:
                continue
            if section_open:
                if ";" in line and "volatile" in line:
                    variable_list.append(self.eval_var_single_line(is_cal_sec, line))
        return variable_list

    def parse_map_file(self,file_path):
        pass

    @staticmethod
    def eval_var_single_line(sec_type, line):
        p = line.strip(";\n").split(" ")
        return VariableContainer(sec_type, p[-1], p[-2])
