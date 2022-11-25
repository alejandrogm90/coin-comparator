#!/usr/bin/env python3

import sqlite3
import pymongo
import json
import sys
sys.path.append("..") 
import commons.commonFunctions as cfs

CONFIG = json.load(open('config.json'))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Númeero de parámetros erroneo.")
        exit(1)

    if not cfs.isDate(sys.argv[1]):
        print("The date entered is erroneous.")
        exit(2)

    SELECTED_DATE = str(sys.argv[1])
    HOST_URL = CONFIG["HOST_URL"]
    ACCESS_KEY = CONFIG["ACCESS_KEY"]
    URL1 = HOST_URL+"/api/list?access_key="+ACCESS_KEY
    URL_MONGODB = CONFIG["URL_MONGODB"]

    myClient = pymongo.MongoClient(URL_MONGODB)
    myDataBase = myClient["coinlayer"]
    myCollection = myDataBase["historical"]

    MY_QUERY_TEXT = { "_id": SELECTED_DATE }

    conn = cfs.create_sqlitle3_connection(CONFIG["SQLITLE_PATH"])
    cur = conn.cursor()
    for element in myCollection.find(MY_QUERY_TEXT):
        for element2 in element["rates"]:
            sql = " INSERT INTO historical (date,name,value) VALUES('"+SELECTED_DATE+"','"+element2+"',"+str(element["rates"][element2])+") "
            try:
                cur.execute(sql)
                conn.commit()
            except sqlite3.Error as e:
                print(e)