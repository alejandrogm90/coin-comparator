#!/usr/bin/env python3

import json
import sqlite3
import sys
import requests

import commons.commonFunctions as cfs

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

    # f1 = open(SELECTED_DATE+".json","r")
    # rdata = f1.json()
    # f1.close()

    finalData = {"_id": SELECTED_DATE, "version": "1", "timestamp": data["timestamp"], "target": data["target"],
        "rates": data["rates"]}

    conn = cfs.create_sqlitle3_connection(CONFIG["SQLITLE_PATH"])
    cur = conn.cursor()
    for element in data["rates"]:
        print(element)
        sql = " INSERT INTO historical (date_part,name,value) "
        sql += " VALUES('" + SELECTED_DATE + "','" + element[0] + "'," + element[1] + ") "
        try:
            cur.execute(sql)
            conn.commit()
        except sqlite3.Error as e:
            print(e)
