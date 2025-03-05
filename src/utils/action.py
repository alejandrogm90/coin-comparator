from enum import Enum

from src.utils.coin import Coin


class ActionType(Enum):
    ERROR = "ERROR"
    SELL = "SELL"
    BUY = "BUY"
    NO_ACTION = "NO_ACTION"


class Movement:
    def __init__(self, coin: Coin, action: ActionType, amount: float, price: float):
        self.coin: Coin = coin
        self.action: ActionType = action
        self.amount: float = amount
        self.price: float = price

    def __str__(self) -> str:
        return f'coin: {self.coin}|action: {self.action}|amount: {self.amount}|price: {self.price}'

    def __dict__(self) -> dict:
        return {
            "coin": self.coin,
            "action": self.action,
            "amount": self.amount,
            "price": self.price
        }

    def get_log(self) -> str:
        return "{0}|{1}|{2:.8f}|{3:.8f}".format(self.coin, self.action, self.amount, self.price)

    def total_price(self) -> float:
        return self.price * self.amount


if __name__ == '__main__':
    print("class CoinWallet")
