import os
import sys

from src.utils.coin_wallet import CoinWallet
from src.utils.common_functions import error_msg, get_file_log, info_msg, load_config, load_json
from src.utils.connector_sqlittle import ConnectorSQLittle

# GLOBALS
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_FILE = f"log/{get_file_log(sys.argv[0])}"
CONFIG = load_config(log_file=LOG_FILE)

if __name__ == '__main__':
    if len(sys.argv) != 6:
        info_msg("Erroneous parameter number.")
        error_msg(1, " [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        con1 = ConnectorSQLittle(CONFIG['SQLITLE_PATH'])
        CONFIG_AGENT = load_json(sys.argv[1])
        sentence = "SELECT value FROM coins_coin_day WHERE date_part <= "
        sentence += f"'{sys.argv[2]}' AND name='{sys.argv[3]}' ORDER BY date_part DESC LIMIT 2"
        rows = con1.get_values(sentence)
        currentPrice = rows[0][0]
        myBank = CoinWallet(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
                            currentPrice)
        print(myBank)
