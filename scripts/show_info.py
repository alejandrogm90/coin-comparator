#!/usr/bin/env python3

import json
import logging.config
import os
import sys

import matplotlib.pyplot as plt

import commons.commonFunctions as cfs

# GLOBALS
# Otra forma es usando os.path.dirname(os.path.abspath(sys.argv[0]))
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + '/config/logging.properties')
LOGGER = logging.getLogger('testLogger')
LOG_FILE = PROJECT_PATH + '/log/' + cfs.getFiletName(sys.argv[0]) + ".log"
CONFIG = json.load(open(PROJECT_PATH + '/config/config_test.json'))


# FUNCTIONS
def coinExist(cur, sdate, name):
    sql = " SELECT count(name) FROM coinlayer_historical WHERE name = '" + name + "' "
    sql = sql + " AND date_part = '" + sdate + "' "

    try:
        cur.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    if cur.fetchone()[0] > 0:
        return True
    else:
        return False


def createImage(cur, sdate, coinList):
    sql = " SELECT name,value FROM coinlayer_historical WHERE date_part = '" + sdate + "' "
    sql += " AND name IN ("
    cont1 = True
    for coin in coinList:
        if cont1:
            sql += "'" + coin + "'"
            cont1 = False
        else:
            sql += ",'" + coin + "'"
    sql += ") "

    try:
        cur.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    l1 = list()
    l2 = list()
    for element in cur:
        print(element)
        l1.append(element[0])
        l2.append(element[1])

    plt.xlabel("Rate Name")
    plt.ylabel("Current Value")
    f = plt.figure()
    N_SIZE = 20
    f.set_figwidth(N_SIZE)
    f.set_figheight(N_SIZE)
    plt.plot(l1, l2)
    plt.savefig(PNG_OUTPUT_LOCATION)  # plt.show()


if __name__ == '__main__':

    if len(sys.argv) < 3:
        cfs.errorMsg(LOGGER, 1, "Erroneous parameter number.Needs [DATE] [COIN]", LOG_FILE)

    SELECTED_DATE = str(sys.argv[1])
    SELECTED_COIN = str(sys.argv[2])
    SQLITLE_LOCATION = CONFIG["SQLITLE_LOCATION"]
    PNG_OUTPUT_LOCATION = CONFIG["PNG_OUTPUT_LOCATION"]

    if not os.path.exists(SQLITLE_LOCATION):
        cfs.errorMsg(LOGGER, 2, "Error sqlite3 database do not exists", LOG_FILE)
    else:
        conn = cfs.create_sqlitle3_connection(SQLITLE_LOCATION)
        cur = conn.cursor()

        # Add Elements
        coinList = list()
        for elemento in range(2, len(sys.argv)):
            if coinExist(cur, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(sys.argv[elemento])
            else:
                LOGGER.warning("Coin '" + sys.argv[elemento] + "' do not exists")

        LOGGER.info(coinList)
        createImage(cur, SELECTED_DATE, coinList)
