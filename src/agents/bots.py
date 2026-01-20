from src.agents.data_connectors.connector_pandas import ConnectorPandas
from src.agents.objects.coin_movement import CoinMovement
from src.agents.objects.wallet_agent import WalletAgent


class Bot1(WalletAgent):
    def __init__(self, config: dict, date: str, coin_name: str, cash: float, coins: float):
        super().__init__(config, date, coin_name, cash, coins)

    def choose(self) -> None:
        c_pandas = ConnectorPandas([self.date.split("-")[0]])
        rows = c_pandas.get_data_frame()

        filter_1 = rows[(rows['date'] <= self.date) & (rows['name'] == self.coin_name)]
        output_data = filter_1.sort_values(by='date', ascending=False).head(2)
        try:
            current_price = float(output_data.iloc[0]['value'])
        except IndexError:
            current_price = 0
        movement = CoinMovement(self.config, self.date, self.coin_name, self.cash, self.coins, current_price)

        if current_price != 0:
            if movement.get_cash() > current_price and CoinMovement.is_decreasing(output_data.values):
                movement.buy_all_coins()
            elif movement.get_coins() > 0 and CoinMovement.is_increasing(output_data.values):
                movement.sell_all_coins()

        self.update_data(movement)

class Bot2(WalletAgent):
    def __init__(self, config: dict, date: str, coin_name: str, cash: float, coins: float):
        super().__init__(config, date, coin_name, cash, coins)

    def choose(self, selected_date: str=None) -> None:
        if not selected_date:
            selected_date = self.date

        c_pandas = ConnectorPandas([selected_date.split("-")[0]])
        rows = c_pandas.get_data_frame()

        filter_1 = rows[(rows['date'] <= selected_date) & (rows['name'] == self.coin_name)]
        output_data = filter_1.sort_values(by='date', ascending=False).head(2)

        try:
            current_price = float(output_data.iloc[0]['value'])
            previous_price = float(output_data.iloc[1]['value'])
        except IndexError:
            current_price = 0
            previous_price = 0

        movement = CoinMovement(self.config, selected_date, self.coin_name, self.cash, self.coins, current_price)

        if current_price != 0 and previous_price != 0:
            if (current_price > (previous_price or movement.get_cash()) and CoinMovement.is_decreasing(rows) and
                    movement.get_buy_difference(movement.get_cash()) > movement.get_buy_tax(
                        movement.get_cash())):
                movement.buy_all_coins()
            elif (current_price < previous_price and movement.get_coins() > 0 and CoinMovement.is_increasing(rows) and
                  movement.get_sell_difference(movement.get_cash()) > movement.get_sell_tax(
                        movement.get_cash())):
                movement.sell_all_coins()

        self.update_data(movement)

