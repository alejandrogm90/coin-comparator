from src.agents.objects.action import ActionType


class CoinMovement:
    def __init__(self, config: dict, c_date: str, coin_name: str, cash: float, coins: float, price: float):
        self.config = dict(config)
        self.c_date = str(c_date)
        self.coin_name = str(coin_name)
        self.cash = float(cash)
        self.coins = float(coins)
        self.price = float(price)
        self.action = ActionType.NO_ACTION

    def __str__(self):
        coin_wallet = f'config: {self.config}, c_date: {self.c_date}, coin_name: {self.coin_name}, cash: {self.cash}'
        coin_wallet += f', coins: {self.coins}, price: {self.price}, action: {self.action.value}'
        return coin_wallet

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

    def show(self) -> None:
        print(self.__dict__())

    def get_log(self) -> str:
        return "{0}|{1}|{2:.8f}|{3:.8f}|{4:.8f}".format(self.c_date, self.action.value, self.cash, self.coins, self.price)

    def get_cash(self) -> float:
        return self.cash

    def get_coins(self) -> float:
        return self.coins

    @staticmethod
    def is_decreasing(rows) -> bool:
        for r1 in range(1, len(rows)):
            if rows[r1][1] < rows[(r1 - 1)][1]:
                return False
        return True

    @staticmethod
    def is_increasing(rows) -> bool:
        for r1 in range(1, len(rows)):
            if rows[r1][1] > rows[(r1 - 1)][1]:
                return False
        return True

    def get_possible_buy_amount(self) -> float:
        costo_total = (1 + self.config["BUY_TAXE"]) * self.price
        return self.cash // costo_total

    def get_possible_sell_amount(self) -> float:
        costo_total = (1 + self.config["SELL_TAXE"]) * self.price
        return self.cash // costo_total

    def buy_all_coins(self) -> None:
        self.buy_coin(self.get_possible_buy_amount())

    def sell_all_coins(self) -> None:
        self.sell_coin(self.coins)

    def get_buy_tax(self, amount) -> float:
        return amount * self.config["BUY_TAXE"]

    def get_sell_tax(self, amount) -> float:
        return amount * self.config["SELL_TAXE"]

    def get_buy_difference(self, amount) -> float:
        local_amount = self.price * amount
        return local_amount - self.get_buy_tax(local_amount)

    def get_sell_difference(self, amount) -> float:
        local_amount = amount * self.price
        return local_amount - self.get_sell_tax(local_amount)

    def buy_coin(self, amount: float) -> None:
        if self.cash > 0 and amount <= self.cash:
            self.cash -= self.get_buy_difference(amount)
            self.coins += amount
            self.action = ActionType.BUY

    def sell_coin(self, amount: float) -> None:
        if self.coins > 0 and amount <= self.coins:
            self.cash += self.get_sell_difference(amount)
            self.coins -= amount
            self.action = ActionType.SELL


if __name__ == '__main__':
    print("class CoinMovement")
