#!/usr/bin/env python3

import logging
import logging.config
import json
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
import commons.commonFunctions as cfs

# GLOBALS
logging.config.fileConfig('logging.conf')
LOGGER = logging.getLogger('testLogger')
CONFIG = json.load(open('config.json'))

# FUNCTIONS
def coinExist(cur, sdate, name):
    sql = " SELECT count(name) FROM coinlayer_historical WHERE name = '"+name+"' "
    sql = sql + " AND date_part = '"+sdate+"' "

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
    sql = " SELECT name,value FROM coinlayer_historical WHERE date_part = '"+sdate+"' "
    sql += " AND name IN ("
    cont1=True
    for coin in coinList:
        if cont1:
            sql += "'"+coin+"'"
            cont1=False
        else:
            sql += ",'"+coin+"'"
    sql += ") "

    try:
        cur.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
            print(e)

    l1=list()
    l2=list()
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
    plt.plot(l1,l2)
    plt.savefig(PNG_OUTPUT_LOCATION)
    #plt.show()


if __name__ == '__main__':

    if len(sys.argv) < 3:
        cfs.errorBreak(LOGGER, 1,"Erroneous parameter number.Needs [DATE] [COIN]")

    SELECTED_DATE = str(sys.argv[1])
    SELECTED_COIN = str(sys.argv[2])
    SQLITLE_LOCATION = CONFIG["SQLITLE_LOCATION"]
    PNG_OUTPUT_LOCATION = CONFIG["PNG_OUTPUT_LOCATION"]

    conn = cfs.create_sqlitle3_connection(SQLITLE_LOCATION)
    cur = conn.cursor()

    # Add Elements
    coinList = list()
    for elemento in range(2,len(sys.argv)):
        if coinExist(cur, SELECTED_DATE, sys.argv[elemento]):
            coinList.append(sys.argv[elemento])
        else:
            LOGGER.warning("Coin '"+sys.argv[elemento]+"' do not exists")

    LOGGER.info(coinList)

    #createImage(cur, SELECTED_DATE, coinList)
    