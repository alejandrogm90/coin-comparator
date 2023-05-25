#!/usr/bin/env python3

from test.coin_wallet_tests import coin_wallet_tests
from test.common_functions_tests import common_functions_tests

if __name__ == '__main__':
    common_functions_tests.main()
    coin_wallet_tests.main()
