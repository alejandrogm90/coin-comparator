import os
import sys

import requests

from src.agents.data_connectors.connector_sqlittle import ConnectorSQLittle
from src.agents.common_utils import CommonFunctions

# GLOBALS
PROJECT_PATH = CommonFunctions.get_project_path()
LOG_FILE = f"log/{CommonFunctions.get_file_log(sys.argv[0])}"
CONFIG = CommonFunctions.load_config(PROJECT_PATH, LOG_FILE)

if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        CommonFunctions.error_msg(1, "Erroneous parameter number.", LOG_FILE)

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

    CommonFunctions.save_json(JSON_PATH, data)

    # Cargar datos desde los ficheros JSON previamente generados
    if os.path.exists(JSON_PATH):
        con1 = ConnectorSQLittle(CONFIG["SQL_PATH"])
        data = CommonFunctions.load_json(JSON_PATH)
        first_part = " INSERT INTO coins_coin_day (id, date_part,name,value) "
        for element in data["rates"]:
            sentence = first_part + " VALUES('" + SELECTED_DATE + "_" + element + "', '" + SELECTED_DATE + (
                "'") + element + "'," + str(data["rates"][element]) + ")"
            con1.execute(sentence)
    else:
        CommonFunctions.error_msg(2, JSON_PATH + " file do not exist", LOG_FILE)
