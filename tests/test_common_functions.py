import unittest

from src.common_utils.common_functions import CommonFunctions


class TestCommonFunctions(unittest.TestCase):
    def setUp(self):
        self.project_path = CommonFunctions.get_project_path()

    def test_get_file_name(self):
        self.assertEqual("s1", CommonFunctions.get_file_name(f"{self.project_path}/scritps/s1.sh"))
        self.assertEqual("s1.sh", CommonFunctions.get_file_name(f"{self.project_path}/scritps/s1.sh", True))

    def test_getHeadLine(self):
        self.assertNotEqual("", CommonFunctions.get_head_line("LEVEL"))

    def test_isDate(self):
        self.assertEqual(True, CommonFunctions.is_valid_date("2022-01-01"))
        self.assertEqual(False, CommonFunctions.is_valid_date("2022-13-01"))
        self.assertEqual(False, CommonFunctions.is_valid_date("2022-01-00"))
        self.assertEqual(False, CommonFunctions.is_valid_date("2022-01-32"))
        self.assertEqual(False, CommonFunctions.is_valid_date("2022-00-01"))

    @classmethod
    def main(cls):
        unittest.main(verbosity=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
