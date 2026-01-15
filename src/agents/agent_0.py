import os
import sys

from src.agents.common_utils import CommonFunctions
from src.agents.data_connectors.connector_sqlittle import ConnectorSQLittle
from src.agents.objects.coin_movement import CoinMovement

# GLOBALS
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_FILE = f"log/{CommonFunctions.get_file_log(sys.argv[0])}"
CONFIG = CommonFunctions.load_config(log_file=LOG_FILE)

if __name__ == '__main__':
    if len(sys.argv) != 6:
        CommonFunctions.info_msg("Erroneous parameter number.")
        CommonFunctions.error_msg(1, " [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        con1 = ConnectorSQLittle(CONFIG['SQL_PATH'])
        CONFIG_AGENT = CommonFunctions.load_json(sys.argv[1])
        sentence = "SELECT value FROM coins_coin_day WHERE date_part <= "
        sentence += f"'{sys.argv[2]}' AND name='{sys.argv[3]}' ORDER BY date_part DESC LIMIT 2"
        rows = con1.get_values(sentence)
        currentPrice = rows[0][0]
        myBank = CoinMovement(CONFIG_AGENT, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
                            currentPrice)
        print(myBank)
