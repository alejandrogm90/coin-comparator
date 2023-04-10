#!/usr/bin/env python3

import json
import logging.config
import os
import sqlite3
import sys

import commons.commonFunctions as cfs

# GLOBALS
# Otra forma es usando os.path.dirname(os.path.abspath(sys.argv[0]))
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + '/config/logging.properties')
LOGGER = logging.getLogger('testLogger')
LOG_FILE = PROJECT_PATH + '/log/' + cfs.getFileLog(sys.argv[0])
CONFIG = json.load(open(PROJECT_PATH + '/config/config_test.json'))


# FUNCTIONS
def coinExist(cur, sdate, name):
    sql = " SELECT count(name) FROM coinlayer_historical WHERE name = '" + name + "' AND date_part = '" + sdate + "' ;"
    try:
        cur.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        cfs.errorMsg(LOGGER, 3, str(e), LOG_FILE)
    if cur.fetchone()[0] > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    info = {
        "name": str(cfs.getFiletName(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print info",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0] + " 2023-05-07 BTC ABC USD"
    }
    cfs.showScriptInfo(info)
    if len(sys.argv) < 3:
        cfs.errorMsg(LOGGER, 1, "Erroneous parameter number.Needs [DATE] [COIN_ARRAY]", LOG_FILE)

    SELECTED_DATE = str(sys.argv[1])
    SQLITLE_LOCATION = CONFIG["SQLITLE_LOCATION"]
    PNG_OUTPUT_LOCATION = CONFIG["PNG_OUTPUT_LOCATION"]

    if not os.path.exists(SQLITLE_LOCATION):
        cfs.errorMsg(LOGGER, 2, "Error sqlite3 database do not exists", LOG_FILE)
    else:
        conn = cfs.create_sqlitle3_connection(SQLITLE_LOCATION)
        cur = conn.cursor()
        coinList = list()
        for elemento in range(2, len(sys.argv)):
            if coinExist(cur, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(sys.argv[elemento])
            else:
                LOGGER.warning("Coin '" + sys.argv[elemento] + "' do not exists")

        LOGGER.info(coinList)
