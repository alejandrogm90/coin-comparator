from test.CoinWallet_tests import coinWalletTests
from test.commonFunctions_tests import commonFunctionsTests

if __name__ == '__main__':
    cw = coinWalletTests()
    cf = commonFunctionsTests()
    # Main
    cw.main()
    cf.main()
