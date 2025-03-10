# !/usr/bin/env python3
import logging.config
import sys

from utils.coin_wallet import CoinWallet

import src.utils.common_functions as cf
import src.utils.connector_sqlittle as cfsql

# GLOBALS
PROJECT_PATH = cf.get_project_path()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cf.get_file_log(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOG_FILE)
MY_QUERY = "SELECT name, value FROM coins_coin_day WHERE date_part <= '{0}' AND name='{1}' " + ("ORDER BY date_part "
                                                                                                "DESC LIMIT 2")
MY_RESPONSE = "{0}|{1}|{2}|{3}"

if __name__ == '__main__':
    if len(sys.argv) != 6:
        cf.info_msg("Erroneous parameter number.")
        cf.error_msg(1, " [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        CONFIG_AGENT = cf.cargar_json(sys.argv[1])
        sentence = MY_QUERY.format(sys.argv[2], sys.argv[3])
        rows = cfsql.get_values(PROJECT_PATH + "/" + CONFIG["SQLITLE_PATH"], sentence)
        currentPrice = rows[0][1]
        myBank = CoinWallet(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
                            currentPrice)

        if myBank.get_cash() > currentPrice and CoinWallet.is_decreasing(rows):
            myBank.buy_all_coins()
        elif myBank.get_coins() > 0 and CoinWallet.is_increasing(rows):
            myBank.sell_all_coins()

        print(myBank)
