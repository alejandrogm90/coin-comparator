#!/usr/bin/env python3

import logging.config
import os
import sys

import requests

import utils.common_functions as cf
import utils.connector_sqlittle as cfsql

# GLOBALS
PROJECT_PATH = cf.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cf.getFileLog(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOGGER, LOG_FILE)

if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        cf.error_msg(1, "Erroneous parameter number.", LOG_FILE)
    
    SELECTED_DATE = str(sys.argv[1])
    SELECTED_YEAR = SELECTED_DATE.split('-')[0]
    JSON_PATH = PROJECT_PATH + "/data/" + SELECTED_YEAR + "/" + SELECTED_DATE + "_coinlayer.json"
    HOST_URL = CONFIG["HOST_URL"]
    ACCESS_KEY = CONFIG["ACCESS_KEY"]
    URL1 = HOST_URL + "/" + SELECTED_DATE + "?access_key=" + ACCESS_KEY

    payload = {}
    headers = {}

    response = requests.request("GET", URL1, headers=headers, data=payload)
    data = response.json()

    cf.guardar_json(JSON_PATH, data)

    # Cargar datos desde los ficheros JSON previamente generados
    if os.path.exists(JSON_PATH):
        data = cf.cargar_json(JSON_PATH)
        first_part = " INSERT INTO coins_coin_day (id, date_part,name,value) "
        for element in data["rates"]:
            sentence = first_part + " VALUES('" + SELECTED_DATE + "_" + element + "', '" + SELECTED_DATE + "','" + \
                element + "'," + str(data["rates"][element]) + ")"
            cfsql.execute(PROJECT_PATH + CONFIG["SQLITLE_PATH"], sentence)
    else:
        cf.error_msg(2, JSON_PATH + " file do not exist", LOG_FILE)
