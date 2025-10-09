import os
import sys
from datetime import datetime
from shutil import copyfile

from dateutil.relativedelta import relativedelta

from src.common_utils.common_functions import CommonFunctions

# GLOBALS
PROJECT_PATH = CommonFunctions.get_project_path()
LOG_FILE = f"{PROJECT_PATH}/log/{CommonFunctions.get_file_log(sys.argv[0])}"
CONFIG = CommonFunctions.load_config(PROJECT_PATH, LOG_FILE)


def replace_basic_file(default_file: str, expected_file: str):
    default_path = PROJECT_PATH + default_file
    expected_file = PROJECT_PATH + expected_file
    print(f'Replace {default_path} for {expected_file}')
    if not os.path.exists(expected_file):
        print("Replaced")
        copyfile(default_path, expected_file)
        return True
    return False


def save_in_json(list_str_dates: list):
    CommonFunctions.info_msg("Saving current month in json ....", LOG_FILE)
    for day in list_str_dates:
        # subprocess.call("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day), shell=True)
        CommonFunctions.debug_msg("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day))
    CommonFunctions.info_msg("Current processed ....", LOG_FILE)


def save_in_sqlittle(list_str_dates: list):
    CommonFunctions.info_msg("Saving current month in sqlittle ....", LOG_FILE)
    for day in list_str_dates:
        # subprocess.call("{0}/src/connector_coinlayer_sqlittle.py {1}".format(PROJECT_PATH, day), shell=True)
        CommonFunctions.debug_msg("{0}/src/connector_coinlayer_sqlittle.py {1}".format(PROJECT_PATH, day))
    CommonFunctions.info_msg("Current processed ....", LOG_FILE)


def save_in_mongodb(list_str_dates: list):
    CommonFunctions.info_msg("Saving current month in mongodb ....", LOG_FILE)
    for day in list_str_dates:
        # subprocess.call("{0}/src/connector_coinlayer_mongodb.py {1}".format(PROJECT_PATH, day), shell=True)
        CommonFunctions.debug_msg("{0}/src/connector_coinlayer_mongodb.py {1}".format(PROJECT_PATH, day))
    CommonFunctions.info_msg("Current processed ....", LOG_FILE)


if __name__ == '__main__':
    info = {
        "name": str(CommonFunctions.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Main script for create all environment",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0]
    }
    CommonFunctions.show_script_info(info)

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        CommonFunctions.error_msg(1, "YEAR MONTH [json, sqlittle]")
    else:
        year: int = 0
        month: int = 0
        try:
            year = int(sys.argv[1])
            if year < 1:
                CommonFunctions.error_msg(1, "MONTH must be > 0 and < 13")
        except ValueError:
            CommonFunctions.error_msg(2, "YEAR must be valid a number")
        try:
            month = int(sys.argv[2])
            if month > 12:
                CommonFunctions.error_msg(3, "MONTH must be > 0 and < 13")
        except ValueError:
            CommonFunctions.error_msg(4, "MONTH must be valid a number")

        # Set connfig
        replace_basic_file('/config/config_example.json', '/config/config.json')
        replace_basic_file('/config/config_agent_example.json', '/config/config_agent.json')
        replace_basic_file('/config/secret_key_example.txt', '/config/secret_key.txt')
        # Set date
        c_date: datetime = datetime(year, month, 1)
        c_date: datetime = c_date - relativedelta(months=+1)
        list_days: list = CommonFunctions.get_list_days(c_date.year, c_date.month)

        # Choose one option
        option: str = sys.argv[3]
        if option == "sqlittle":
            save_in_sqlittle(list_days)
        elif option == "json":
            save_in_json(list_days)
        else:
            CommonFunctions.error_msg(5, "A valid option must be send [json, sqlittle] ")
