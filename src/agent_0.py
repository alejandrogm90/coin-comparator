#!/usr/bin/env python3
import json
import sys
import logging.config

import commons.common_functions as cfs
import commons.common_functions_SQLITLE as cfsql

from commons.coin_wallet import CoinWallet

# GLOBALS
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cfs.getFileLog(sys.argv[0])
CONFIG = cfs.load_config(PROJECT_PATH, LOGGER, LOG_FILE)
MY_QUERY = "SELECT * FROM coinlayer_historical WHERE date <= '{0}' AND name='{1}' ORDER BY date DESC LIMIT 2"
MY_RESPONSE = "{0}|{1}|{2}|{3}"

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print(sys.argv)
        print("Erroneous parameter number.")
        exit(1)
    else:
        f1 = open(sys.argv[1])
        CONFIG_AGENT = json.load(f1)
        f1.close()
        myBank = CoinWallet(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]))
        sentence = MY_QUERY.format(sys.argv[2], sys.argv[3])
        rows = cfsql.get_values(CONFIG["SQLITLE_PATH"], sentence)
        currentPrice = rows[0][2]

        print(MY_RESPONSE.format(
            str(myBank),
            str(currentPrice),
            str(CoinWallet.isDecreasing(rows)),
            CoinWallet.isIncreasing(rows))
        )
