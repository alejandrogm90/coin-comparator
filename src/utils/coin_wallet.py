#!/usr/bin/env python3
from enum import Enum


class ActionType(Enum):
    ERROR = "ERROR"
    SELL = "SELL"
    BUY = "BUY"
    NO_ACTION = "NO_ACTION"


class CoinWallet:
    def __init__(self, config: dict, c_date: str, coin_name: str, cash: float, coins: float, price: float):
        self.config = dict(config)
        self.c_date = str(c_date)
        self.coin_name = str(coin_name)
        self.cash = float(cash)
        self.coins = float(coins)
        self.price = float(price)
        self.action = ActionType.NO_ACTION

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "config": self.config,
            "c_date": self.c_date,
            "coin_name": self.coin_name,
            "cash": self.cash,
            "coins": self.coins,
            "price": self.price,
            "action": self.action
            }

    def get_log(self):
        return "{0}|{1}|{2:.8f}|{3:.8f}".format(self.c_date, self.action, self.cash, self.coins)

    @staticmethod
    def is_decreasing(rows):
        for r1 in range(1, len(rows)):
            if rows[r1][1] < rows[(r1 - 1)][1]:
                return False
        return True

    @staticmethod
    def is_increasing(rows):
        for r1 in range(1, len(rows)):
            if rows[r1][1] > rows[(r1 - 1)][1]:
                return False
        return True

    def buy_all_coins(self):
        self.buy_coin(self.cash)

    def sell_all_coins(self):
        self.sell_coin(self.coins)

    def get_buy_tax(self, amount):
        return amount * self.config["BUY_TAXE"]

    def get_sell_tax(self, amount):
        return amount * self.config["SELL_TAXE"]

    def get_buy_difference(self, amount):
        local_amount = amount % self.price
        return local_amount - self.get_buy_tax(local_amount)

    def get_sell_difference(self, amount):
        local_amount = (amount * self.price)
        return local_amount - self.get_sell_tax(local_amount)

    def buy_coin(self, amount):
        if self.cash > 0 and amount <= self.cash:
            self.cash = self.get_buy_difference(amount)
            self.coins += (amount / self.price)
            self.action = ActionType.BUY
        else:
            self.action = ActionType.ERROR

    def sell_coin(self, amount):
        if self.coins > 0 and amount <= self.coins:
            self.cash += self.get_sell_difference(amount)
            self.coins -= amount
            self.action = ActionType.SELL
        else:
            self.action = ActionType.ERROR


if __name__ == '__main__':
    print("class CoinWallet")
