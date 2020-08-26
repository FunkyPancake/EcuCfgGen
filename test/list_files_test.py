import unittest
from src.Parser import Parser
from src.VariableContainer import VariableContainer
from lxml import etree


class ParserTests(unittest.TestCase):
    def test_list_c_files(self):
        expected = ["/test_src/measurement.c", "/test_src/measurement2.c", "/test_src/test_src_rec/test_cal.c",
                    "/test_src/measurement_1Line.c"]
        expected.sort()
        p = Parser()
        actual = p.list_files("G:/projects/MicraEcu/SW/EcuCfgGen/test", ".c")
        self.assertEqual(expected, actual)

    def test_extract_variables(self):
        file = "/test_src/measurement.c"
        p = Parser()
        actual = p.parse_c_file("G:/projects/MicraEcu/SW/EcuCfgGen/test/test_src/measurement_1Line.c")
        expected = [VariableContainer("Measurement", "test_16", "sint16")]
        self.assertEqual(expected, actual)

    def test_serialize(self):
        expected = b'<Entry>\n  <NAME>TEST_01</NAME>\n</Entry>\n'
        xml_obj = VariableContainer("Measurement", "TEST_01", "sint16").serialize()
        actual = etree.tostring(xml_obj,pretty_print=True)

        self.assertEqual(expected, actual)

    def test_parse_map(self):
        path = "G:/projects/MicraEcu/SW/EcuCfgGen/test/ppc.map"
        p = Parser()
        cfg = [VariableContainer("Measurement", "TEST_02", "sint16"),VariableContainer("Measurement", "TEST_01", "sint16")]
        p.parse_map_file(path,cfg)
        self.assertEqual(cfg[0].address,0x40008000)
        self.assertEqual(cfg[1].address,0x40008000)


if __name__ == '__main__':
    unittest.main()
