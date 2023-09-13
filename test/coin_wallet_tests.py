#!/usr/bin/env python3
import json
import unittest

import src.commons.common_functions as cfs
from src.commons.coin_wallet import CoinWallet


class coin_wallet_tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        f1 = open(cfs.getProjetPath() + '/config/config_agent_example.json')
        cls.CONFIG_AGENT = json.load(f1)
        f1.close()

    @classmethod
    def tearDownClass(cls):
        cls.CONFIG_AGENT = ""

    def test_action(self):
        coin_wallet1 = CoinWallet(self.CONFIG_AGENT, "2022-01-01", "BTC", 111.11, 222.22, 333.33)
        self.assertEqual("2022-01-01", coin_wallet1.cDate)
        self.assertEqual("BTC", coin_wallet1.coinName)
        self.assertEqual(111.11, coin_wallet1.cash)
        self.assertEqual(222.22, coin_wallet1.coins)
        self.assertEqual(333.33, coin_wallet1.price)
        self.assertEqual("NONE", coin_wallet1.action)
        self.assertEqual(self.CONFIG_AGENT, coin_wallet1.config)

    def test_buyAllCoins(self):
        coin_wallet1 = CoinWallet(self.CONFIG_AGENT, "2022-01-01", "BTC", 300, 12, 100)
        coin_wallet1.buyAllCoins()
        self.assertEqual("BUY", coin_wallet1.action)
        self.assertEqual(0, coin_wallet1.cash)
        self.assertEqual(15, coin_wallet1.coins)

    def test_sellAllCoins(self):
        coin_wallet1 = CoinWallet(self.CONFIG_AGENT, "2022-01-01", "BTC", 300, 3, 100)
        coin_wallet1.sellAllCoins()
        self.assertEqual("SELL", coin_wallet1.action)
        self.assertEqual(600, coin_wallet1.cash)
        self.assertEqual(0, coin_wallet1.coins)

    @classmethod
    def main(cls):
        unittest.main(verbosity=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
