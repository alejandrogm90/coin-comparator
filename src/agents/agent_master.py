import sys

from src.common_utils.common_functions import CommonFunctions
from src.common_utils.connector_sqlittle import ConnectorSQLittle
from src.objects.coin_wallet import CoinWallet


class AgentMaster:
    def __init__(self, log_file: str):
        self.log_file = log_file
        self.config = CommonFunctions.load_config(log_file=self.log_file)
        self.config_agent = CommonFunctions.load_json(sys.argv[1])
        con1 = ConnectorSQLittle(self.config['SQLITLE_PATH'])
        sentence = "SELECT value FROM coins_coin_day WHERE date_part <= "
        sentence += f"'{sys.argv[2]}' AND name='{sys.argv[3]}' ORDER BY date_part DESC LIMIT 2"
        rows = con1.get_values(sentence)
        currentPrice = rows[0][0]
        myBank = CoinWallet(self.config_agent, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
                            currentPrice)
        myBank.show()
