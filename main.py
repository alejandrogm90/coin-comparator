import os
import sys
from datetime import datetime
from shutil import copyfile

from dateutil.relativedelta import relativedelta

from src.utils.common_functions import debug_msg, error_msg, get_file_log, get_file_name, get_list_days, \
    get_project_path, info_msg, load_config, show_script_info

# GLOBALS
PROJECT_PATH = get_project_path()
LOG_FILE = f"{PROJECT_PATH}/log/{get_file_log(sys.argv[0])}"
CONFIG = load_config(PROJECT_PATH, LOG_FILE)


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
    info_msg("Saving current month in json ....", LOG_FILE)
    for day in list_str_dates:
        # subprocess.call("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day), shell=True)
        debug_msg("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day))
    info_msg("Current processed ....", LOG_FILE)


def save_in_sqlittle(list_str_dates: list):
    info_msg("Saving current month in sqlittle ....", LOG_FILE)
    for day in list_str_dates:
        # subprocess.call("{0}/src/connector_coinlayer_sqlittle.py {1}".format(PROJECT_PATH, day), shell=True)
        debug_msg("{0}/src/connector_coinlayer_sqlittle.py {1}".format(PROJECT_PATH, day))
    info_msg("Current processed ....", LOG_FILE)


def save_in_mongodb(list_str_dates: list):
    info_msg("Saving current month in mongodb ....", LOG_FILE)
    for day in list_str_dates:
        # subprocess.call("{0}/src/connector_coinlayer_mongodb.py {1}".format(PROJECT_PATH, day), shell=True)
        debug_msg("{0}/src/connector_coinlayer_mongodb.py {1}".format(PROJECT_PATH, day))
    info_msg("Current processed ....", LOG_FILE)


if __name__ == '__main__':
    info = {
        "name": str(get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Main script for create all environment",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0]
    }
    show_script_info(info)

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        error_msg(1, "YEAR MONTH [json, sqlittle]")
    else:
        year: int = 0
        month: int = 0
        try:
            year = int(sys.argv[1])
            if year < 1:
                error_msg(1, "MONTH must be > 0 and < 13")
        except ValueError:
            error_msg(2, "YEAR must be valid a number")
        try:
            month = int(sys.argv[2])
            if month > 12:
                error_msg(3, "MONTH must be > 0 and < 13")
        except ValueError:
            error_msg(4, "MONTH must be valid a number")

        # Set connfig
        replace_basic_file('/config/config_example.json', '/config/config.json')
        replace_basic_file('/config/config_agent_example.json', '/config/config_agent.json')
        replace_basic_file('/config/secret_key_example.txt', '/config/secret_key.txt')
        # Set date
        c_date: datetime = datetime(year, month, 1)
        c_date: datetime = c_date - relativedelta(months=+1)
        list_days: list = get_list_days(c_date.year, c_date.month)

        # Choose one option
        option: str = sys.argv[3]
        if option == "sqlittle":
            save_in_sqlittle(list_days)
        elif option == "json":
            save_in_json(list_days)
        else:
            error_msg(5, "A valid option must be send [json, sqlittle] ")
