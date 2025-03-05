import os
import sqlite3
import sys

import matplotlib.pyplot as plt
import pandas

import src.utils.common_functions as cf
from src.utils.connector_sqlittle import ConnectorSQLittle

# GLOBALS
PROJECT_PATH = cf.get_project_path()
LOG_FILE = PROJECT_PATH + '/log/' + cf.get_file_log(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOG_FILE)


# FUNCTIONS
def exist_coin(conn, sdate, name):
    sql = " SELECT count(name) FROM coinlayer_historical WHERE name = '" + name + "' AND date_part = '" + sdate + "' ;"
    try:
        conn.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        cf.error_msg(3, str(e), LOG_FILE)
    if conn.fetchone()[0] > 0:
        return True
    else:
        return False


def create_image(cur, sdate, coinList):
    sql = " SELECT name,value FROM coinlayer_historical WHERE date_part = '" + sdate + "' AND name IN ("
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
    n_size = 20
    f.set_figwidth(n_size)
    f.set_figheight(n_size)
    plt.plot(l1, l2)
    plt.savefig(PNG_OUTPUT_LOCATION)  # plt.show()


if __name__ == '__main__':
    info = {
        "name": str(cf.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print graphics",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0] + " output.png 2023-05-07 BTC ABC USD"
    }
    cf.show_script_info(info)

    # PARAMETERS
    if len(sys.argv) < 4:
        cf.error_msg(1, "Erroneous parameter number.Needs [OUTPUT_FILE] [DATE] [COIN_ARRAY]", LOG_FILE)

    PNG_OUTPUT_LOCATION = str(sys.argv[1])
    SELECTED_DATE = str(sys.argv[2])
    SQLITLE_PATH = CONFIG["SQLITLE_PATH"]

    if not os.path.exists(SQLITLE_PATH):
        cf.error_msg(2, "Error sqlite3 database do not exists", LOG_FILE)
    else:
        connector = ConnectorSQLittle(SQLITLE_PATH)
        df1 = pandas.read_sql_query(connector.connect)
        coinList = list()
        for elemento in range(3, len(sys.argv)):
            if exist_coin(connector.connect, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(sys.argv[elemento])
            else:
                cf.warn_msg("Coin '" + sys.argv[elemento] + "' do not exists")

        cf.info_msg(str(coinList))
        create_image(connector.connect, SELECTED_DATE, coinList)
