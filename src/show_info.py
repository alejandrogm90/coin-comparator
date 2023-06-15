#!/usr/bin/env python3

import json
import logging.config
import os
import sys

import commons.common_functions as cfs
import commons.common_functions_SQLITLE as cfsql

# GLOBALS
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + '/config/logging.properties')
LOGGER = logging.getLogger('testLogger')
LOG_FILE = PROJECT_PATH + '/log/' + cfs.getFileLog(sys.argv[0])
CONFIG = cfs.load_config(PROJECT_PATH, LOGGER, LOG_FILE)


if __name__ == '__main__':
    info = {
        "name": str(cfs.getFiletName(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print info",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0] + " 2023-05-07 BTC ABC USD"
    }
    cfs.showScriptInfo(info)
    
    # PARAMETERS
    if len(sys.argv) < 3:
        cfs.errorMsg(LOGGER, 1, "Erroneous parameter number.Needs [DATE] [COIN_ARRAY]", LOG_FILE)

    SELECTED_DATE = str(sys.argv[1])
    SQLITLE_PATH = PROJECT_PATH + CONFIG["SQLITLE_PATH"]

    if not os.path.exists(SQLITLE_PATH):
        cfs.errorMsg(LOGGER, 2, "Error sqlite3 database do not exists: " + SQLITLE_PATH , LOG_FILE)
    else:
        coinList = list()
        for elemento in range(2, len(sys.argv)):
            if cfsql.coinExist(SQLITLE_PATH, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(sys.argv[elemento])
            else:
                LOGGER.warning("Coin '" + sys.argv[elemento] + "' do not exists")
        if len(coinList) > 0:
            LOGGER.info(coinList)

