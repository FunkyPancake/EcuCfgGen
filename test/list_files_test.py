import unittest
from src.Parser import Parser
from src.VariableContainer import VariableContainer


class ParserTests(unittest.TestCase):
    def test_list_c_files(self):
        expected = ["/test_src/measurement.c", "/test_src/measurement2.c", "/test_src/test_src_rec/test_cal.c", "/test_src/measurement_1Line.c"]
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


if __name__ == '__main__':
    unittest.main()
