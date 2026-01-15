import os
import sys

from src.agents import common_utils as cfsql
from src.agents.common_utils import CommonFunctions

# GLOBALS
PROJECT_PATH = CommonFunctions.get_project_path()
LOG_FILE = PROJECT_PATH + '/log/' + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(PROJECT_PATH, LOG_FILE)

if __name__ == '__main__':
    info = {
        "name": str(CommonFunctions.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print info",
        "Author": "Alejandro Gómez",
        "parameters": [f'{sys.argv[0]}  2023-05-07 BTC ABC USD']
    }
    CommonFunctions.show_script_info(info)

    SQL_PATH = PROJECT_PATH + CONFIG["SQL_PATH"]

    if not os.path.exists(SQL_PATH):
        CommonFunctions.error_msg(2, "Error sqlite3 database do not exists: " + SQL_PATH, LOG_FILE)
    else:
        con1 = cfsql.ConnectorSQLittle(SQL_PATH)
        rows = con1.get_values("SELECT DISTINCT date_part FROM coins_coin_day;")
        for row in rows:
            print(row[0])

