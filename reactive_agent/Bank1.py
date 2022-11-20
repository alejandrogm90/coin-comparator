#!/usr/bin/env python3

import sqlite3
import json
import sys
sys.path.append("..") 
import commons.commonFunctions as cfs

CONFIG = json.load(open('config.json'))

class Bank1:
    def __init__(self, cDate, coinName, cash, coins, price):
        self.cDate = cDate
        self.coinName = coinName
        self.cash = cash
        self.coins = coins
        self.action = "NONE"
        self.price = price
        self.CONFIG_TEST = json.load(open('config-agent_test.json'))

    @staticmethod
    def getValues(sentence):
        conn = cfs.create_sqlitle3_connection(CONFIG["SQLITLE_LOCATION"])
        cur = conn.cursor()
        rows = ""
        try:
            cur.execute(sentence)
            rows = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        return rows

    @staticmethod
    def isDecreasing(rows):
        for r1 in range(1, len(rows)):
            if rows[r1][2] < rows[(r1 - 1)][2]:
                return False
        return True

    @staticmethod
    def isIncreasing(rows):
        for r1 in range(1, len(rows)):
            if rows[r1][2] > rows[(r1 - 1)][2]:
                return False
        return True

    def getCash(self):
        return self.cash

    def getCoins(self):
        return self.coins

    def getBuyTaxeAmount(self, amount):
        return amount * self.CONFIG_TEST["BUY_TAXE"]

    def getSellTaxeAmount(self, amount):
        return amount * self.CONFIG_TEST["SELL_TAXE"]

    def getBuyGanances(self,amount):
        localAmount = (amount / self.price)
        return localAmount - self.getBuyTaxeAmount(localAmount)

    def getSellGanances(self,amount):
        localAmount = (amount * self.price)
        return localAmount - self.getSellTaxeAmount(localAmount)

    def buyAllCoins(self):
        self.coins = self.getBuyGanances(self.cash)
        self.cash = self.cash % self.price
        self.action = "BUY"

    def sellAllCoins(self):
        self.cash = self.getSellGanances(self.coins)
        self.coins = 0
        self.action = "SELL"

    def buyCoins(self,amount):
        if self.cash > 0 and amount <= self.cash:
            self.coins = self.getBuyGanances(amount)
            self.cash = amount % self.price
            self.action = "BUY"
        else:
            self.action = "ERROR-BUY"

    def sellCoins(self,amount):
        if self.coins > 0 and amount <= self.coins:
            self.cash = self.getSellGanances(amount)
            self.coins = self.coins - amount
            self.action = "SELL"
        else:
            self.action = "ERROR-SELL"

    def __str__(self) -> str:
        return self.cDate+"|"+self.action+"|{0:.8f}".format(self.cash)+"|{0:.8f}".format(self.coins)


if __name__ == '__main__':
    print("class Bank")
