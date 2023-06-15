#!/usr/bin/env python3

import pandas
import logging.config
import os
import sys

import commons.common_functions as cfs

# GLOBALS
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + "/config/logging.properties")
LOGGER = logging.getLogger("testLogger")
LOG_FILE = PROJECT_PATH + "/log/" + cfs.getFileLog(sys.argv[0])
CONFIG = cfs.load_config(PROJECT_PATH, LOGGER, LOG_FILE)

if __name__ == '__main__':
    info = {
        "name": str(cfs.getFiletName(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Create a complete data file of a year in CSV and JSON",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0] + " 2023 coinlayer"
    }
    cfs.showScriptInfo(info)

    # PARAMETERS
    if len(sys.argv) != 3:
        cfs.infoMsg(LOGGER, sys.argv[0]+" [YEAR] [SOURCE]", LOG_FILE)
        cfs.errorMsg(LOGGER, 1, "Erroneous parameter number.", LOG_FILE)

    # Constants
    SELECTED_YEAR = str(sys.argv[1])
    SELECTED_SOURCE = str("_"+sys.argv[2]+".json")
    JSON_DIRECTORY = PROJECT_PATH + "/data/"
    DATA_DIRECTORY = JSON_DIRECTORY + SELECTED_YEAR + "/"
    OUTPUT_DIRECTORY = JSON_DIRECTORY + "dataFrames/"

    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    # Main dataFrame
    MY_COLUMNS = ["date", "name", "value"]
    df_pandas = pandas.DataFrame(columns=MY_COLUMNS)

    if os.path.exists(DATA_DIRECTORY):
        LIST_FILES = os.listdir(DATA_DIRECTORY)
        LIST_FILES.sort()
        for file1 in LIST_FILES:
            if SELECTED_SOURCE in file1:
                file_name = DATA_DIRECTORY + file1
                cfs.infoMsg(LOGGER, "Loading file: "+file1)
                data = cfs.cargar_json(file_name)
                # For each value in a day
                for element in data["rates"]:
                    df_pandas.loc[len(df_pandas)] = [data["date"], element, data["rates"][element]]
        # Write data to output file
        OUTPUT_NAME = sys.argv[2] + "_" + SELECTED_YEAR
        OUTPUT_PATH = OUTPUT_DIRECTORY + OUTPUT_NAME
        # df_pandas.to_csv(OUTPUT_PATH + ".csv", index=False)
        df_pandas.to_csv(OUTPUT_PATH + ".csv")
        df_pandas.to_json(OUTPUT_PATH + ".json")
        df_pandas.to_excel(OUTPUT_PATH + ".xlsx")
        df_pandas.to_parquet(OUTPUT_PATH + ".parquet", partition_cols=MY_COLUMNS)
        cfs.infoMsg(LOGGER, OUTPUT_NAME + " has been saved.", LOG_FILE)
    else:
        cfs.errorMsg(LOGGER, 2, DATA_DIRECTORY + " directory do not exist", LOG_FILE)