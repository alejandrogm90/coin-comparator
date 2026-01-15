import sys
import unittest

from src.agents.common_utils.common_functions import CommonFunctions


class TestCommonFunctions(unittest.TestCase):
    @classmethod
    def main(cls):
        unittest.main(verbosity=2)

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

    def test_ddd(self):
        print("")
        info = {
            "name": str(CommonFunctions.get_file_name(sys.argv[0], True)),
            "location": sys.argv[0],
            "description": "Description test",
            "author": "test maker",
            "parameters": ["Example parameters 1", f"Example parameters 2", "Example parameters 3"]
        }
        assert CommonFunctions.show_script_info(info) is None
        assert CommonFunctions.show_script_info({"location": sys.argv[0]}) is None
        assert CommonFunctions.show_script_info() is None


if __name__ == '__main__':
    unittest.main(verbosity=2)
