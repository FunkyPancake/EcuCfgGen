from xml import etree


def create_cfg(self, base_src_path, map_path, out_path):
    cfg = []
    for file in self.list_files(base_src_path, '.c'):
        self.parse_c_file(file, cfg)
    self.parse_map_file(map_path, cfg)
    cfg_xml = etree.Element("Config")
    cfg_xml.write(out_path if '.xml' in out_path else out_path + '.xml')


def update_cfg(self, map_path, out_path):
    cfg = []