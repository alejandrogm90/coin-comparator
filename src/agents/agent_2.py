import logging.config
import sys

from src.common_utils.common_functions import CommonFunctions
from src.common_utils.connector_sqlittle import ConnectorSQLittle
from src.objects.coin_wallet import CoinWallet

# GLOBALS
PROJECT_PATH = CommonFunctions.get_project_path()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(PROJECT_PATH, LOG_FILE)
MY_QUERY = "SELECT name, value FROM coins_coin_day WHERE date_part <= '{0}' AND name='{1}' " + ("ORDER BY date_part "
                                                                                                "DESC LIMIT 4")
MY_RESPONSE = "{0}|{1}|{2}|{3}"

if __name__ == '__main__':
    if len(sys.argv) != 6:
        CommonFunctions.info_msg("Erroneous parameter number.")
        CommonFunctions.error_msg(1, " [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        CONFIG_AGENT = CommonFunctions.load_json(sys.argv[1])
        sentence = MY_QUERY.format(sys.argv[2], sys.argv[3])
        rows = ConnectorSQLittle.get_values(PROJECT_PATH + "/" + CONFIG["SQLITLE_PATH"], sentence)
        currentPrice = rows[0][1]
        previousPrice = rows[1][1]
        myBank = CoinWallet(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
                            currentPrice)

        if currentPrice > (previousPrice or myBank.get_cash()) and CoinWallet.is_decreasing(
                rows) and myBank.get_buy_difference(myBank.get_cash()) > myBank.get_buy_tax(myBank.get_cash()):
            myBank.buy_all_coins()
        elif currentPrice < previousPrice and myBank.get_coins() > 0 and CoinWallet.is_increasing(
                rows) and myBank.get_sell_difference(myBank.get_cash()) > myBank.get_sell_tax(myBank.get_cash()):
            myBank.sell_all_coins()

        print(myBank)
