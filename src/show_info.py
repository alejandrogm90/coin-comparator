import os
import sys

import src.utils.common_functions as cf
import src.utils.connector_sqlittle as cfsql

# GLOBALS
PROJECT_PATH = cf.get_project_path()

LOG_FILE = PROJECT_PATH + '/log/' + cf.get_file_log(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOG_FILE)

if __name__ == '__main__':
    info = {
        "name": str(cf.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print info",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0] + " 2023-05-07 BTC ABC USD"
    }
    cf.show_script_info(info)

    # PARAMETERS
    if len(sys.argv) < 3:
        cf.error_msg(1, "Erroneous parameter number.Needs [DATE] [COIN_ARRAY]", LOG_FILE)

    SELECTED_DATE = str(sys.argv[1])
    SQLITLE_PATH = PROJECT_PATH + CONFIG["SQLITLE_PATH"]

    if not os.path.exists(SQLITLE_PATH):
        cf.error_msg(2, "Error sqlite3 database do not exists: " + SQLITLE_PATH, LOG_FILE)
    else:
        coinList = list()
        for elemento in range(2, len(sys.argv)):
            if cfsql.exist_coin(SQLITLE_PATH, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(sys.argv[elemento])
            else:
                cf.warn_msg("Coin '" + sys.argv[elemento] + "' do not exists")
        if len(coinList) > 0:
            cf.info_msg(coinList)
