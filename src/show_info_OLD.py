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

    # PARAMETERS
    if len(sys.argv) < 3:
        CommonFunctions.error_msg(1, "Erroneous parameter number.Needs [DATE] [COIN_ARRAY]", LOG_FILE)

    SELECTED_DATE = str(sys.argv[1])
    SQL_PATH = PROJECT_PATH + CONFIG["SQL_PATH"]

    if not os.path.exists(SQL_PATH):
        CommonFunctions.error_msg(2, "Error sqlite3 database do not exists: " + SQL_PATH, LOG_FILE)
    else:
        coin_list = []
        for elemento in range(2, len(sys.argv)):
            if cfsql.exist_coin(SQL_PATH, SELECTED_DATE, sys.argv[elemento]):
                coin_list.append(sys.argv[elemento])
            else:
                CommonFunctions.warn_msg("Coin '" + sys.argv[elemento] + "' do not exists")
        if len(coin_list) > 0:
            CommonFunctions.info_msg(str(coin_list))
