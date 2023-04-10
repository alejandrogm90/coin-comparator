import unittest

import src.commons.commonFunctions as cfs


class commonFunctionsTests(unittest.TestCase):
    def test_getFiletName(self):
        self.assertEqual("s1", cfs.getFiletName("scritps/s1.sh"))
        self.assertEqual("s1.sh", cfs.getFiletName("scritps/s1.sh", True))

    def test_getHeadLine(self):
        self.assertNotEqual("", cfs.getHeadLine("LEVEL"))


    def test_isDate(self):
        self.assertEqual(True, cfs.isDate("2022-01-01"))
        self.assertEqual(False, cfs.isDate("2022-13-01"))
        self.assertEqual(False, cfs.isDate("2022-01-00"))
        self.assertEqual(False, cfs.isDate("2022-01-32"))
        self.assertEqual(False, cfs.isDate("2022-00-01"))


    @classmethod
    def main(cls):
        unittest.main()


if __name__ == '__main__':
    unittest.main()
