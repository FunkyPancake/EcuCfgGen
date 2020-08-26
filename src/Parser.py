import os
import re
from src.VariableContainer import VariableContainer
from lxml import etree


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def list_files(root_path, extension):
        file_list = []
        for root, dirs, files in os.walk(root_path):
            [file_list.append(f"{root.split(root_path)[1]}/{file}".replace("\\", "/")) for file in files if
             extension in file]
        return file_list

    @staticmethod
    def eval_var_single_line(sec_type, line):
        p = line.strip(";\n").split(" ")
        return VariableContainer(sec_type, p[-1], p[-2])

    @staticmethod
    def eval_var_multi_line(sec_type, lines):
        pass

    def parse_c_file(self, file_path):
        variable_list = []
        if not os.path.exists(file_path):
            return
        fd = open(file_path, "r")
        for line in fd.readlines():
            if "START_SEC_VAR" in line:
                is_cal_sec = "CAL" in line
                section_open = True
                continue
            if "STOP_SEC_VAR" in line:
                section_open = False
                continue
            if "#include" in line:
                continue
            if section_open:
                if ";" in line and "volatile" in line:
                    variable_list.append(self.eval_var_single_line(is_cal_sec, line))
        fd.close()
        return variable_list

    @staticmethod
    def parse_map_file( file_path, cfg_to_update):
        if not os.path.exists(file_path):
            return
        pattern = "  ([0-9A-Fa-f]+) (?P<byte_size>[0-9A-Fa-f]+) (?P<address>[0-9A-Fa-f]+) ([0-9A-Fa-f]+)  (\d) (?P<name>\w+)"
        fd = open(file_path, "r")
        for line in fd.readlines():
            match = re.search(pattern, line)
            if not match:
                continue
            for entry in cfg_to_update:
                if entry.name == match.group('name'):
                    entry.address = int(match.group('address'), 16)
                    entry.byte_size = int(match.group('byte_size'), 16)
        fd.close()

    def create_cfg(self,base_src_path,map_path, out_path):
        cfg = []
        for file in self.list_files(base_src_path,'.c'):
            self.parse_c_file(file,cfg)
        self.parse_map_file(map_path,cfg)
        cfg_xml = etree.Element("Config")
        cfg_xml.write(out_path if '.xml' in out_path else out_path+'.xml')

    def update_cfg(self,map_path, out_path):
        cfg = []