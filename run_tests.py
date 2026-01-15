from tests.test_coin_movement import TestCoinMovement
from tests.test_common_functions import TestCommonFunctions
from tests.test_connector_pandas import TestConnectorPandas
from tests.test_wallet import TestWallet

if __name__ == '__main__':
    TestCommonFunctions.main()
    TestCoinMovement.main()
    TestWallet.main()
    TestConnectorPandas.main()
