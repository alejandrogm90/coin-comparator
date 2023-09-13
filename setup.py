#!/usr/bin/env python3
import logging.config
import subprocess
import sys
import os
from shutil import copyfile

from dateutil.relativedelta import relativedelta

import src.commons.common_functions as cfs

# GLOBALS
PROJECT_PATH = cfs.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + '/config/logging.properties')
LOGGER = logging.getLogger('testLogger')
LOG_FILE = PROJECT_PATH + '/log/' + cfs.getFileLog(sys.argv[0])
CONFIG = cfs.load_config(PROJECT_PATH, LOGGER, LOG_FILE)


def replace_basic_file(default_file: str, explected_file: str):
    print(f'Replace {default_file} for {explected_file}')
    if (not os.path.exists(explected_file)):
        print("Replaced")
        copyfile(default_file, explected_file)
        return True
    return False


def main():
    replace_basic_file(PROJECT_PATH + '/config/config_example.json', PROJECT_PATH + '/config/config.json')
    replace_basic_file(PROJECT_PATH + '/config/config_agent_example.json', PROJECT_PATH + '/config/config_agent.json')
    replace_basic_file(PROJECT_PATH + '/config/secret_key_example.txt', PROJECT_PATH + '/config/secret_key.txt')
    cfs.infoMsg(LOGGER, "Getting current month ....", LOG_FILE)
    c_date = cfs.getDatetime()
    c_date = c_date - relativedelta(months=+1)
    for day in cfs.get_list_days(c_date.year, c_date.month):
        subprocess.call("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day), shell=True)
    cfs.infoMsg(LOGGER, "Getting current month ....", LOG_FILE)
    c_date = cfs.getDatetime()
    for day in cfs.get_list_days(c_date.year, c_date.month):
        subprocess.call("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day), shell=True)
        if cfs.getDate() == day:
            break
    cfs.infoMsg(LOGGER, "Current month saved ....", LOG_FILE)


if __name__ == '__main__':
    info = {
        "name": str(cfs.getFiletName(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Main script for create all environment",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0]
    }
    cfs.showScriptInfo(info)

    main()
