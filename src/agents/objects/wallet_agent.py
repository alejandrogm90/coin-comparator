from .coin_movement import CoinMovement


class WalletAgent:
    def __init__(self, config: dict, date: str, coin_name: str, cash: float, coins: float):
        self.config = config
        self.date = date
        self.coin_name = coin_name
        self.cash = cash
        self.coins = coins
        self.movement_list: list[CoinMovement] = []

    def __dict__(self):
        return {
            "config": self.config,
            "date": self.date,
            "coin_name": self.coin_name,
            "cash": self.cash,
            "coins": self.coins,
            "movement_list": [m1 for m1 in self.movement_list]
        }

    def __str__(self):
        full_log = ""
        for l1 in self.movement_list:
            full_log += f"{l1.get_log()}\n"
        return full_log

    @staticmethod
    def print_argv_error() -> None:
        print("PARAMETERS must be [ config_path: str, date: str, coin_name: str, cash: float, coins: float ]")

    def update_data(self, cm: CoinMovement):
        self.cash = cm.cash
        self.coins = cm.coins
        self.movement_list.append(cm)


    def get_last_movement(self) -> CoinMovement | None:
        if len(self.movement_list) > 0:
            return self.movement_list[len(self.movement_list)-1]
        else:
            return None
