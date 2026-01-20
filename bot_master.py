import sys

from src.agents.common_utils.common_functions import CommonFunctions
from src.agents.bots import Bot1, Bot2

if __name__ == '__main__':
    if len(sys.argv) != 7:
        CommonFunctions.info_msg("Erroneous parameter number.")
        CommonFunctions.error_msg(1, "[AGENT_NUMBER] [CONFIG_AGENT] [DATE] [COIN_NAME] [CASH] [COINS]")
    else:
        current_bot = None
        AGENT_NUMBER = sys.argv[1]
        CONFIG_AGENT = CommonFunctions.load_json(sys.argv[2])
        DATE = sys.argv[3]
        COIN_NAME = sys.argv[4]
        CASH = float(sys.argv[5])
        COINS = float(sys.argv[6])

        if AGENT_NUMBER == "1":
            print(f"AGENT_NUMBER={AGENT_NUMBER}")
            print(f"CONFIG_AGENT={CONFIG_AGENT}")
            print(f"DATE={DATE}")
            print(f"COIN_NAME={COIN_NAME}")
            print(f"CASH={CASH}")
            print(f"CASH={CASH}")

        if AGENT_NUMBER == "1":
            current_bot = Bot1(CONFIG_AGENT, DATE, COIN_NAME, CASH, COINS)
        elif AGENT_NUMBER == "2":
            current_bot = Bot2(CONFIG_AGENT, DATE, COIN_NAME, CASH, COINS)
        else:
            print(f"Error: Invalid bot number ({AGENT_NUMBER}).")

        if current_bot:
            current_bot.choose()
            print(current_bot)
