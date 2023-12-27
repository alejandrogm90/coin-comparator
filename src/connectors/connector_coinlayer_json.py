#!/usr/bin/env python3

import logging.config
import os.path
import sys
import requests

import utils.common_functions as cf

# GLOBALS
PROJECT_PATH = cf.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cf.getFileLog(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOG_FILE)

def save_day_in_json(SELECTED_DATE):
    SELECTED_YEAR = SELECTED_DATE.split('-')[0]
    JSON_PATH = PROJECT_PATH + "/data/" + SELECTED_YEAR + "/" + SELECTED_DATE + "_coinlayer.json"
    if (not os.path.exists(JSON_PATH)):
        HOST_URL = CONFIG["HOST_URL"]
        ACCESS_KEY = CONFIG["ACCESS_KEY"]
        URL1 = HOST_URL + "/" + SELECTED_DATE + "?access_key=" + ACCESS_KEY

        payload = {}
        headers = {}

        response = requests.request("GET", URL1, headers=headers, data=payload)
        data = response.json()

        cf.guardar_json(JSON_PATH, data)
        cf.info_msg("DATA SAVED IN: {0}".format(JSON_PATH), LOG_FILE)
    else:
        cf.info_msg("FILE ALREADY EXISTS IN: {0}".format(JSON_PATH), LOG_FILE)


if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        cf.error_msg(1, "Erroneous parameter number.", LOG_FILE)

    save_day_in_json(str(sys.argv[1]))
