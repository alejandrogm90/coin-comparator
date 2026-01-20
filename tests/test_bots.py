import unittest
from unittest.mock import patch, MagicMock

import pandas

from src.agents.bots import Bot1


class TestBot1(unittest.TestCase):

    @patch('src.agents.bots.ConnectorPandas')
    @patch('src.agents.bots.CoinMovement')
    def test_choose_buy_coins(self, mock_coin_movement, mock_connector_pandas):
        # Simular datos de prueba
        mock_data = MagicMock()

        mock_data.get_data_frame.return_value = pandas.DataFrame({
            'date': ['2026-01-20', '2026-01-19'],
            'name': ['Bitcoin', 'Bitcoin'],
            'value': [10, 500]
        })

        mock_connector_pandas.return_value = mock_data

        # Configurar el movimiento de monedas simulado
        mock_movement = mock_coin_movement.return_value
        mock_movement.get_cash.return_value = 1000
        mock_movement.get_coins.return_value = 0

        bot = Bot1(config={}, date='2026-01-20', coin_name='Bitcoin', cash=1000, coins=0)
        bot.choose()

        # Verificar que se llamara a comprar todas las monedas
        mock_movement.buy_all_coins.assert_called_once()

    @patch('src.agents.bots.ConnectorPandas')
    @patch('src.agents.bots.CoinMovement')
    def test_choose_sell_coins(self, mock_coin_movement, mock_connector_pandas):
        # Simular datos de prueba
        mock_data = MagicMock()
        mock_data.get_data_frame.return_value = pandas.DataFrame({
            'date': ['2026-01-20', '2026-01-19'],
            'name': ['Bitcoin', 'Bitcoin'],
            'value': [60000, 50000]
        })

        mock_connector_pandas.return_value = mock_data

        # Configurar el movimiento de monedas simulado
        mock_movement = mock_coin_movement.return_value
        mock_movement.get_cash.return_value = 0
        mock_movement.get_coins.return_value = 10

        bot = Bot1(config={}, date='2026-01-20', coin_name='Bitcoin', cash=0, coins=10)
        bot.choose()

        # Verificar que se llamara a vender todas las monedas
        mock_movement.sell_all_coins.assert_called_once()

    @patch('src.agents.bots.ConnectorPandas')
    @patch('src.agents.bots.CoinMovement')
    def test_choose_no_action(self, mock_coin_movement, mock_connector_pandas):
        # Simular datos de prueba
        mock_data = MagicMock()
        mock_data.get_data_frame.return_value = pandas.DataFrame({
            'date': ['2026-01-20', '2026-01-19'],
            'name': ['Bitcoin', 'Bitcoin'],
            'value': [0, 0]
        })

        mock_connector_pandas.return_value = mock_data

        # Configurar el movimiento de monedas simulado
        mock_movement = mock_coin_movement.return_value
        mock_movement.get_cash.return_value = 1000
        mock_movement.get_coins.return_value = 0

        bot = Bot1(config={}, date='2026-01-20', coin_name='Bitcoin', cash=1000, coins=0)
        bot.choose()

        # Verificar que no se llamara a comprar o vender
        mock_movement.buy_all_coins.assert_not_called()
        mock_movement.sell_all_coins.assert_not_called()

    @classmethod
    def main(cls):
        unittest.main()


if __name__ == '__main__':
    unittest.main()
