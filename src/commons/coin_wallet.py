#!/usr/bin/env python3

class CoinWallet:
    def __init__(self, config, cDate, coinName, cash, coins, price):
        self.config = config
        self.cDate = cDate
        self.coinName = coinName
        self.cash = cash
        self.coins = coins
        self.price = price
        self.action = "NONE"

    @staticmethod
    def isDecreasing(rows):
        for r1 in range(1, len(rows)):
            if rows[r1][1] < rows[(r1 - 1)][1]:
                return False
        return True

    @staticmethod
    def isIncreasing(rows):
        for r1 in range(1, len(rows)):
            if rows[r1][1] > rows[(r1 - 1)][1]:
                return False
        return True

    def getCash(self):
        return self.cash

    def getCoins(self):
        return self.coins

    def buyAllCoins(self):
        self.buyCoins(self.cash)

    def sellAllCoins(self):
        self.sellCoins(self.coins)

    def getBuyTaxeAmount(self, amount):
        return amount * self.config["BUY_TAXE"]

    def getSellTaxeAmount(self, amount):
        return amount * self.config["SELL_TAXE"]

    def getBuyGanances(self, amount):
        localAmount = amount % self.price
        return localAmount - self.getBuyTaxeAmount(localAmount)

    def getSellGanances(self, amount):
        localAmount = (amount * self.price)
        return localAmount - self.getSellTaxeAmount(localAmount)

    def buyCoins(self, amount):
        print("{0}|{1}|{2}".format(self.getBuyGanances(amount), amount, self.price))
        if self.cash > 0 and amount <= self.cash:
            self.cash = self.getBuyGanances(amount)
            self.coins += (amount / self.price)
            self.action = "BUY"
        else:
            self.action = "ERROR-BUY"

    def sellCoins(self, amount):
        if self.coins > 0 and amount <= self.coins:
            self.cash += self.getSellGanances(amount)
            self.coins -= amount
            self.action = "SELL"
        else:
            self.action = "ERROR-SELL"

    def __str__(self) -> str:
        return "{0}|{1}|{2:.8f}|{3:.8f}".format(self.cDate, self.action, self.cash, self.coins)


if __name__ == '__main__':
    print("class CoinWallet")
