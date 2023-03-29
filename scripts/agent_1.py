#!/usr/bin/env python3

import sys

from commons.CoinWallet import CoinWallet

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print(sys.argv)
        print("Erroneous parameter number.")
        exit(1)
    else:
        myBank = CoinWallet(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
        sentence = "SELECT * FROM coinlayer_historical WHERE date <= '" + sys.argv[1] + "' AND name='" + sys.argv[
            2] + "' ORDER BY date DESC LIMIT 2"
        rows = CoinWallet.getValues(sentence)
        currentPrice = rows[0][2]

        if myBank.getCash() > currentPrice and CoinWallet.isDecreasing(rows):
            myBank.buyAllCoins()
        elif myBank.getCoins() > 0 and CoinWallet.isIncreasing(rows):
            myBank.sellAllCoins()

        print(str(myBank) + "|" + str(currentPrice) + "|DES=" + str(CoinWallet.isDecreasing(rows)) + "|ASC=" + str(
            CoinWallet.isIncreasing(rows)))
