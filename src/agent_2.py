#!/usr/bin/env python3

import sys

from commons.coin_wallet import CoinWallet
from src.commons.common_functions_SQLITLE import get_values

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print(sys.argv)
        print("Erroneous parameter number.")
        exit(1)
    else:
        myBank = CoinWallet(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
        sentence = "SELECT * FROM coinlayer_historical WHERE date <= '" + sys.argv[1] + "' AND name='" + sys.argv[
            2] + "' ORDER BY date DESC LIMIT 4 "
        rows = get_values(CONFIG_AGENT["SQLITLE_PATH"], sentence)
        previousPrice = rows[1][2]
        currentPrice = rows[0][2]

        if currentPrice > (previousPrice or myBank.getCash()) and CoinWallet.isDecreasing(
                rows) and myBank.getBuyGanances(myBank.getCash()) > myBank.getBuyTaxeAmount(myBank.getCash()):
            myBank.buyAllCoins()
        elif currentPrice < previousPrice and myBank.getCoins() > 0 and CoinWallet.isIncreasing(
                rows) and myBank.getSellGanances(myBank.getCash()) > myBank.getSellTaxeAmount(myBank.getCash()):
            myBank.sellAllCoins()

        print(str(myBank) + "|" + str(currentPrice))
