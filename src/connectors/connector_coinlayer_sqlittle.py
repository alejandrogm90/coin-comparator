import os
import sys

import requests

from src.utils.common_functions import error_msg, get_file_log, load_config, load_json, save_json
from src.utils.connector_sqlittle import ConnectorSQLittle

# GLOBALS
LOG_FILE = f"log/{get_file_log(sys.argv[0])}"
CONFIG = load_config(PROJECT_PATH, LOG_FILE)

if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        error_msg(1, "Erroneous parameter number.", LOG_FILE)

    SELECTED_DATE = str(sys.argv[1])
    SELECTED_YEAR = SELECTED_DATE.split('-')[0]
    JSON_PATH = f"data/{SELECTED_YEAR}/{SELECTED_DATE}_coinlayer.json"
    HOST_URL = CONFIG["HOST_URL"]
    ACCESS_KEY = CONFIG["ACCESS_KEY"]
    URL1 = HOST_URL + "/" + SELECTED_DATE + "?access_key=" + ACCESS_KEY

    payload = {}
    headers = {}

    response = requests.request("GET", URL1, headers=headers, data=payload)
    data = response.json()

    save_json(JSON_PATH, data)

    # Cargar datos desde los ficheros JSON previamente generados
    if os.path.exists(JSON_PATH):
        con1 = ConnectorSQLittle(CONFIG["SQLITLE_PATH"])
        data = load_json(JSON_PATH)
        first_part = " INSERT INTO coins_coin_day (id, date_part,name,value) "
        for element in data["rates"]:
            sentence = first_part + " VALUES('" + SELECTED_DATE + "_" + element + "', '" + SELECTED_DATE + (
                "'") + element + "'," + str(data["rates"][element]) + ")"
            con1.execute(sentence)
    else:
        error_msg(2, JSON_PATH + " file do not exist", LOG_FILE)
