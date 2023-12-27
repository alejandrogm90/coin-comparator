#!/usr/bin/env python3
import json
import unittest
from pprint import pprint

from src.utils.coin_wallet import CoinWallet, ActionType


class CoinWalletTests(unittest.TestCase):
    def setUp(self):
        f1 = open("config/config_agent_example.json")
        self.CONFIG_AGENT = json.load(f1)
        f1.close()
        self.initial_cash = 100.00
        self.initial_coins = 10.00
        self.initial_price = 20.00
        self.coin_wallet1 = CoinWallet(self.CONFIG_AGENT, "2022-01-01", "BTC", self.initial_cash, self.initial_coins,
            self.initial_price)

    def tearDown(self):
        self.CONFIG_AGENT = ""

    def test_data(self):
        self.assertEqual("2022-01-01", self.coin_wallet1.c_date)
        self.assertEqual("BTC", self.coin_wallet1.coin_name)
        self.assertEqual(self.initial_cash, self.coin_wallet1.cash)
        self.assertEqual(self.initial_coins, self.coin_wallet1.coins)
        self.assertEqual(self.initial_price, self.coin_wallet1.price)
        self.assertEqual(ActionType.NO_ACTION, self.coin_wallet1.action, "Action is not {0}".format(ActionType.NO_ACTION))
        self.assertEqual(self.CONFIG_AGENT, self.coin_wallet1.config, "Configs are not equals")

    def buy_error(self):
        self.coin_wallet1.buy_all_coins()
        self.coin_wallet1.buy_all_coins()
        print(self.coin_wallet1.__dict__())
        self.assertEqual(ActionType.NO_ACTION, self.coin_wallet1.action, "Action is not {0}".format(ActionType.BUY))
        self.assertEqual(0, self.coin_wallet1.cash)

    def test_buy_all_coins(self):
        self.coin_wallet1.buy_all_coins()
        self.assertEqual(ActionType.BUY, self.coin_wallet1.action, "Action is not {0}".format(ActionType.BUY))
        self.assertEqual(0, self.coin_wallet1.cash)
        # self.assertEqual(15, self.coin_wallet1.coins)

    def test_sell_all_coins(self):
        self.coin_wallet1.sell_all_coins()
        self.assertEqual(ActionType.SELL, self.coin_wallet1.action, "Action is not {0}".format(ActionType.SELL))
        # self.assertEqual(600, self.coin_wallet1.cash)
        self.assertEqual(0, self.coin_wallet1.coins)


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main()
