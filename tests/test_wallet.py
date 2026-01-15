import json
import unittest

from src.agents.common_utils.common_functions import CommonFunctions
from src.agents.objects.wallet import Wallet


class TestWallet(unittest.TestCase):
    def setUp(self):
        self.project_path = CommonFunctions.get_project_path()
        f1 = open(f"{self.project_path}/config/config_agent_example.json")
        self.CONFIG_AGENT = json.load(f1)
        f1.close()
        self.wallet_1 = Wallet()

    def tearDown(self):
        self.CONFIG_AGENT = ""

    def test_data(self):
        self.assertEqual(0.0, self.wallet_1.cash, "Default cash different to 0.0")
        #self.assertEqual([], self.wallet_1.coins, "Default coins different to []")


    @classmethod
    def main(cls):
        unittest.main(verbosity=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
