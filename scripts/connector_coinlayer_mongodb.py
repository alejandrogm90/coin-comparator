#!/usr/bin/env python3

import json
import sys

import pymongo
import requests

CONFIG = json.load(open('config-example.json'))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Erroneous parameter number.")
        exit(1)

    SELECTED_DATE = str(sys.argv[1])
    HOST_URL = CONFIG["HOST_URL"]
    ACCESS_KEY = CONFIG["ACCESS_KEY"]
    URL1 = HOST_URL + "/" + SELECTED_DATE + "?access_key=" + ACCESS_KEY
    URL_MONGODB = CONFIG["URL_MONGODB"]

    payload = {}
    headers = {}

    response = requests.request("GET", URL1, headers=headers, data=payload)
    data = response.json()

    finalData = {"_id":SELECTED_DATE, "version":"1", "timestamp":data["timestamp"], "target":data["target"],
        "rates":data["rates"]}

    myClient = pymongo.MongoClient(URL_MONGODB)
    myDataBase = myClient["coinlayer"]
    myCollection = myDataBase["historical"]

    MY_QUERY_TEXT = {"_id":SELECTED_DATE}
    if myCollection.count_documents(MY_QUERY_TEXT) > 0:
        x = myCollection.replace_one(MY_QUERY_TEXT, finalData)
    else:
        x = myCollection.insert_one(finalData)
