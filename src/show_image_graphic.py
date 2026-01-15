import os
import sqlite3
import sys

import matplotlib.pyplot as plt
import pandas

from src.agents.data_connectors.connector_sqlittle import ConnectorSQLittle
from src.agents.common_utils import CommonFunctions

# GLOBALS
PROJECT_PATH = CommonFunctions.get_project_path()
LOG_FILE = PROJECT_PATH + '/log/' + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(PROJECT_PATH, LOG_FILE)


# FUNCTIONS
def exist_coin(conn: ConnectorSQLittle, sdate: str, name: str):
    sql = f"SELECT count(name) FROM coinlayer_historical WHERE name='{name}' AND date_part='{sdate}' ;"

    try:
        conn_result = conn.execute(sql)
        if conn_result.fetchone()[0] > 0:
            return True
    except sqlite3.Error as e:
        CommonFunctions.error_msg(3, str(e), LOG_FILE)
    return False


def create_image(conn, sdate, coinList):
    sql = f"SELECT name,value FROM coinlayer_historical WHERE date_part='{sdate}' AND name IN ("
    cont1 = True
    for coin in coinList:
        if cont1:
            sql += f"'{coin}'"
            cont1 = False
        else:
            sql += f",'{coin}'"
    sql += ") "

    conn_result = conn.execute(sql)

    l1 = list()
    l2 = list()
    for element in conn_result:
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
        "name": str(CommonFunctions.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print graphics",
        "Author": "Alejandro Gómez",
        "parameters": [f'{sys.argv[0]}  output.png 2023-05-07 BTC ABC USD']
    }
    CommonFunctions.show_script_info(info)

    # PARAMETERS
    if len(sys.argv) < 4:
        CommonFunctions.error_msg(1, "Erroneous parameter number.Needs [OUTPUT_FILE] [DATE] [COIN_ARRAY]", LOG_FILE)

    PNG_OUTPUT_LOCATION = str(sys.argv[1])
    SELECTED_DATE = str(sys.argv[2])
    SQL_PATH = CONFIG["SQL_PATH"]

    if not os.path.exists(SQL_PATH):
        CommonFunctions.error_msg(2, "Error sqlite3 database do not exists", LOG_FILE)
    else:
        connector = ConnectorSQLittle(SQL_PATH)
        df1 = pandas.read_sql_query(connector)
        coinList = list()
        for elemento in range(3, len(sys.argv)):
            if exist_coin(connector.connect, SELECTED_DATE, sys.argv[elemento]):
                coinList.append(sys.argv[elemento])
            else:
                CommonFunctions.warn_msg(f"Coin '{sys.argv[elemento]}' do not exists")

        CommonFunctions.info_msg(str(coinList))
        create_image(connector.connect, SELECTED_DATE, coinList)
