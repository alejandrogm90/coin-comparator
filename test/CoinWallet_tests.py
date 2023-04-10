import unittest

from src.commons.CoinWallet import CoinWallet
import src.commons.commonFunctions as cfs

PROJECT_PATH = cfs.getProjetPath()

class coinWalletTests(unittest.TestCase):
    def test_action(self):
        coin_wallet1 = CoinWallet("2022-01-01", "BTC", 111.11, 222.22, 333.33)
        self.assertEqual("2022-01-01", coin_wallet1.cDate)
        self.assertEqual("BTC", coin_wallet1.coinName)
        self.assertEqual(111.11, coin_wallet1.cash)
        self.assertEqual(222.22, coin_wallet1.coins)
        self.assertEqual(333.33, coin_wallet1.price)
        self.assertEqual("NONE", coin_wallet1.action)
        self.assertNotEqual("", coin_wallet1.CONFIG_TEST)

    @classmethod
    def main(cls):
        unittest.main()


if __name__ == '__main__':
    unittest.main()
