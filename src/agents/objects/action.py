from enum import Enum

from .coin import Coin


class ActionType(Enum):
    NO_ACTION = "NO_ACTION"
    SELL = "SELL"
    BUY = "BUY"


class Movement:
    def __init__(self, coin: Coin=Coin(), action: ActionType=ActionType.NO_ACTION, amount: float=0, price: float=0):
        self.coin: Coin = coin
        self.action: ActionType = action
        self.amount: float = amount
        self.price: float = price

    def __str__(self) -> str:
        return f'coin: {self.coin}|action: {self.action.value}|amount: {self.amount}|price: {self.price}'

    def __dict__(self) -> dict:
        return {
            "coin": self.coin,
            "action": self.action,
            "amount": self.amount,
            "price": self.price
        }

    def get_log(self) -> str:
        return "{0}|{1}|{2:.8f}|{3:.8f}".format(self.coin, self.action.value, self.amount, self.price)

    def total_price(self) -> float:
        return self.price * self.amount


if __name__ == '__main__':
    print("class CoinMovement")
