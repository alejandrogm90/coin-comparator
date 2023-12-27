#!/usr/bin/env python3
import sys
import logging.config

import utils.common_functions as cf
import utils.connector_sqlittle as cfsql

from utils.coin_wallet import CoinWallet

# GLOBALS
PROJECT_PATH = cf.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cf.getFileLog(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOGGER, LOG_FILE)
MY_QUERY = "SELECT * FROM coins_coin_day WHERE date_part <= '{0}' AND name='{1}' ORDER BY date_part DESC LIMIT 2"

if __name__ == '__main__':
    if len(sys.argv) != 6:
        cf.info_msg("Erroneous parameter number.")
        cf.error_msg(1, " [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        CONFIG_AGENT = cf.cargar_json(sys.argv[1])
        sentence = MY_QUERY.format(sys.argv[2], sys.argv[3])
        rows = cfsql.get_values(PROJECT_PATH + "/" + CONFIG["SQLITLE_PATH"], sentence)
        currentPrice = rows[0][2]
        myBank = CoinWallet(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
            currentPrice)

        print(myBank)
