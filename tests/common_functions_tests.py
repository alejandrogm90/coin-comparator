#!/usr/bin/env python3

import unittest

import src.utils.common_functions as cf


class TesCommonFunctions(unittest.TestCase):
    def test_getFiletName(self):
        self.assertEqual("s1", cf.get_file_name("scritps/s1.sh"))
        self.assertEqual("s1.sh", cf.get_file_name("scritps/s1.sh", True))

    def test_getHeadLine(self):
        self.assertNotEqual("", cf.get_head_line("LEVEL"))

    def test_isDate(self):
        self.assertEqual(True, cf.is_valid_date("2022-01-01"))
        self.assertEqual(False, cf.is_valid_date("2022-13-01"))
        self.assertEqual(False, cf.is_valid_date("2022-01-00"))
        self.assertEqual(False, cf.is_valid_date("2022-01-32"))
        self.assertEqual(False, cf.is_valid_date("2022-00-01"))

    @classmethod
    def main(cls):
        unittest.main(verbosity=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
