import unittest
from binary_con import bin_converter


class TestBinary_Con(unittest.TestCase):
    
    # tests for converting binary to decimal
    def test_binary_to_decimal(self):
        self.assertEqual(bin_converter('bd', 1001), 9)
        self.assertEqual(bin_converter('bd', 101), 5)

    # tests for converting binary to binary
    def test_binary_to_binary(self):
        self.assertEqual(bin_converter('db', 90), 1011010)
        self.assertEqual(bin_converter('db', 44), 101100)


if __name__ == '__main__':
    unittest.main()
