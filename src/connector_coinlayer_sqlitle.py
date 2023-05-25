#!/usr/bin/env python3

import json
import logging.config
import os
import sys

import requests

import commons.common_functions as cfs
import commons.common_functions_SQL as cfsql

# GLOBALS
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cfs.getFileLog(sys.argv[0])
CONFIG = cfs.load_config(PROJECT_PATH, LOGGER, LOG_FILE)

if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        cfs.errorMsg(LOGGER, 1, "Erroneous parameter number.", LOG_FILE)
    
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

    cfs.guardar_json(JSON_PATH, data)

    first_part = "INSERT INTO coins_coinlayer_historical (date_part,name,value) "
    for element in data["rates"]:
        sentence = first_part + " VALUES('" + SELECTED_DATE + "','" + element + "'," + str(data["rates"][element]) + ")"
        print(PROJECT_PATH + CONFIG["SQLITLE_PATH"])
        cfsql.execute(PROJECT_PATH + CONFIG["SQLITLE_PATH"], sentence)
