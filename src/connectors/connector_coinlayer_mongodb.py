#!/usr/bin/env python3

import logging.config
import sys

import pymongo
import requests

import utils.common_functions as cf

# GLOBALS
PROJECT_PATH = cf.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cf.getFileLog(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOGGER, LOG_FILE)

if __name__ == "__main__":
    # PARAMETERS
    if len(sys.argv) != 2:
        cf.error_msg(1, "Erroneous parameter number.", LOG_FILE)
    
    SELECTED_DATE = str(sys.argv[1])
    SELECTED_YEAR = SELECTED_DATE.split('-')[0]
    JSON_PATH = PROJECT_PATH + "/data/" + SELECTED_YEAR + "/" + SELECTED_DATE + "_coinlayer.json"
    HOST_URL = CONFIG["HOST_URL"]
    ACCESS_KEY = CONFIG["ACCESS_KEY"]
    URL1 = HOST_URL + "/" + SELECTED_DATE + "?access_key=" + ACCESS_KEY
    URL_MONGODB = CONFIG["URL_MONGODB"]

    payload = {}
    headers = {}

    response = requests.request("GET", URL1, headers=headers, data=payload)
    data = response.json()

    cf.guardar_json(JSON_PATH, data)

    if data == "":
        cf.error_msg(1, "Default configuration have to be replaced", LOG_FILE)

    finalData = {
        "_id": SELECTED_DATE,
        "rates": data["rates"]
    }

    myClient = pymongo.MongoClient(URL_MONGODB)
    myDataBase = myClient["coinlayer"]
    myCollection = myDataBase["historical"]

    MY_QUERY_TEXT = {
        "_id": SELECTED_DATE
    }
    x = "NONE"
    if myCollection.count_documents(MY_QUERY_TEXT) > 0:
        x = myCollection.replace_one(MY_QUERY_TEXT, finalData)
    else:
        x = myCollection.insert_one(finalData)
