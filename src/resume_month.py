import os
import sys

import pandas as pd

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
    JUST_MONTH = SELECTED_DATE[0:7]
    SQL_PATH = PROJECT_PATH + CONFIG["SQL_PATH"]

    if not os.path.exists(SQL_PATH):
        CommonFunctions.error_msg(2, "Error sqlite3 database do not exists: " + SQL_PATH, LOG_FILE)
    else:
        coinList = []
        for elemento in range(2, len(sys.argv)):
            if cfsql.exist_coin(SQL_PATH, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(str(sys.argv[elemento]))
            else:
                CommonFunctions.warn_msg("Coin '" + sys.argv[elemento] + "' do not exists")
        if len(coinList) > 0:
            CommonFunctions.info_msg(coinList)
            coin_df = pd.DataFrame(columns=['date_part', 'name', 'value'])
            for coin in coinList:
                sql = ("SELECT date_part, name, value FROM coins_coin_day WHERE name = '" + coin + ("' AND date_part "
                                                                                                    "LIKE '") +
                       JUST_MONTH + "%' ;")
                print(sql)
                for new_row in cfsql.get_values(SQL_PATH, sql):
                    current_row = [new_row[0], new_row[1], new_row[2]]
                    coin_df.loc[len(coin_df)] = current_row
            print(coin_df)
