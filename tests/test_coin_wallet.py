import json
import unittest

from src.utils.coin_wallet import ActionType, CoinWallet
from src.utils.common_functions import get_project_path


class TestCoinWallet(unittest.TestCase):
    def setUp(self):
        self.project_path = get_project_path()
        f1 = open(f"{self.project_path}/config/config_agent_example.json")
        self.CONFIG_AGENT = json.load(f1)
        f1.close()
        self.c_date = "2022-01-01"
        self.coin_name = "BTC"
        self.initial_cash = 100.00
        self.initial_coins = 10.00
        self.initial_price = 20.00
        self.coin_wallet1 = CoinWallet(self.CONFIG_AGENT, self.c_date, self.coin_name, self.initial_cash,
                                       self.initial_coins, self.initial_price)

    def tearDown(self):
        self.CONFIG_AGENT = ""

    def test_data(self):
        self.assertEqual(self.c_date, self.coin_wallet1.c_date)
        self.assertEqual(self.coin_name, self.coin_wallet1.coin_name)
        self.assertEqual(self.initial_cash, self.coin_wallet1.cash)
        self.assertEqual(self.initial_coins, self.coin_wallet1.coins)
        self.assertEqual(self.initial_price, self.coin_wallet1.price)
        self.assertEqual(ActionType.NO_ACTION, self.coin_wallet1.action,
                         "Action is not {0}".format(ActionType.NO_ACTION))
        self.assertEqual(self.CONFIG_AGENT, self.coin_wallet1.config, "Configs are not equals")

    def buy_error(self):
        self.coin_wallet1.buy_all_coins()
        self.coin_wallet1.buy_all_coins()
        self.assertEqual(ActionType.NO_ACTION, self.coin_wallet1.action, "Action is not {0}".format(ActionType.BUY))
        self.assertEqual(0, self.coin_wallet1.cash)

    def test_buy_all_coins(self):
        self.coin_wallet1.buy_all_coins()
        self.assertEqual(ActionType.BUY, self.coin_wallet1.action, "Action is not {0}".format(ActionType.BUY))
        self.assertEqual(0, self.coin_wallet1.cash)  # self.assertEqual(15, self.coin_wallet1.coins)

    def test_sell_all_coins(self):
        self.coin_wallet1.sell_all_coins()
        self.assertEqual(ActionType.SELL, self.coin_wallet1.action, "Action is not {0}".format(ActionType.SELL))
        # self.assertEqual(600, self.coin_wallet1.cash)
        self.assertEqual(0, self.coin_wallet1.coins)


    @classmethod
    def main(cls):
        unittest.main(verbosity=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
