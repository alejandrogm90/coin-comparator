#!/usr/bin/env python3
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
MY_QUERY = "SELECT name, value FROM coins_coin_day WHERE date_part <= '{0}' AND name='{1}' " + \
           "ORDER BY date_part DESC LIMIT 4"
MY_RESPONSE = "{0}|{1}|{2}|{3}"

if __name__ == '__main__':
    if len(sys.argv) != 6:
        cfs.infoMsg(LOGGER, "Erroneous parameter number.")
        cfs.errorMsg(LOGGER, 1, " [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        CONFIG_AGENT = cfs.cargar_json(sys.argv[1])
        sentence = MY_QUERY.format(sys.argv[2], sys.argv[3])
        rows = cfsql.get_values(PROJECT_PATH + "/" + CONFIG["SQLITLE_PATH"], sentence)
        currentPrice = rows[0][1]
        previousPrice = rows[1][1]
        myBank = CoinWallet(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
            currentPrice)

        if currentPrice > (previousPrice or myBank.getCash()) and CoinWallet.isDecreasing(
                rows) and myBank.getBuyGanances(myBank.getCash()) > myBank.getBuyTaxeAmount(myBank.getCash()):
            myBank.buyAllCoins()
        elif currentPrice < previousPrice and myBank.getCoins() > 0 and CoinWallet.isIncreasing(
                rows) and myBank.getSellGanances(myBank.getCash()) > myBank.getSellTaxeAmount(myBank.getCash()):
            myBank.sellAllCoins()

        print(myBank)
