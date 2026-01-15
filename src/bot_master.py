import sys

from src.agents.bot_1 import Bot1
from src.agents.common_utils import CommonFunctions

if __name__ == '__main__':
    if len(sys.argv) != 7:
        CommonFunctions.info_msg("Erroneous parameter number.")
        CommonFunctions.error_msg(1, "[AGENT_NUMBER] [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        AGENT_NUMBER = sys.argv[1]
        CONFIG_AGENT = CommonFunctions.load_json(sys.argv[2])
        DATE = sys.argv[3]
        COIN_NAME = sys.argv[4]
        CASH = float(sys.argv[5])
        COINS = float(sys.argv[6])

        if AGENT_NUMBER == "1":
            current_bot = Bot1(CONFIG_AGENT,DATE,COIN_NAME,CASH,COINS)