import sys

from src.agents.common_utils.common_functions import CommonFunctions
from src.agents.data_connectors.connector_pandas import ConnectorPandas
from src.agents.objects.wallet_agent import WalletAgent
from src.agents.objects.coin_movement import CoinMovement


class Bot2(WalletAgent):
    def __init__(self, config: dict, date: str, coin_name: str, cash: float, coins: float):
        super().__init__(config, date, coin_name, cash, coins)

    def choose(self) -> None:
        c_pandas = ConnectorPandas([self.date.split("-")[0]])
        rows = c_pandas.get_data_frame()

        filter_1 = rows[(rows['date'] <= self.date) & (rows['name'] == self.coin_name)]
        output_data = filter_1.sort_values(by='date', ascending=False).head(2)

        current_price = float(output_data.iloc[0]['value'])
        previous_price = float(output_data.iloc[1]['value'])
        movement = CoinMovement(self.config, self.date, self.coin_name, self.cash, self.coins, current_price)

        if (current_price > (previous_price or movement.get_cash()) and CoinMovement.is_decreasing(rows) and
                movement.get_buy_difference(movement.get_cash()) > movement.get_buy_tax(
                    movement.get_cash())):
            movement.buy_all_coins()
        elif (current_price < previous_price and movement.get_coins() > 0 and CoinMovement.is_increasing(rows) and
              movement.get_sell_difference(movement.get_cash()) > movement.get_sell_tax(
                    movement.get_cash())):
            movement.sell_all_coins()

        self.update_data(movement)

if __name__ == '__main__':
    if len(sys.argv) != 6:
        WalletAgent.print_argv_error()
        exit(1)

    bot = Bot2(CommonFunctions.load_json(sys.argv[1]), sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]))
    bot.choose()
    print(bot)
