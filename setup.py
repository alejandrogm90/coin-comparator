#!/usr/bin/env python3
import logging.config
import subprocess
import sys
import os
from shutil import copyfile

from dateutil.relativedelta import relativedelta

import src.utils.common_functions as cf

# GLOBALS
PROJECT_PATH = cf.getProjetPath()
logging.config.fileConfig(PROJECT_PATH + '/config/logging.properties')
LOGGER = logging.getLogger('testLogger')
LOG_FILE = PROJECT_PATH + '/log/' + cf.getFileLog(sys.argv[0])
CONFIG = cf.load_config(PROJECT_PATH, LOGGER, LOG_FILE)


def replace_basic_file(default_file: str, explected_file: str):
    default_path = PROJECT_PATH + default_file
    explected_path = PROJECT_PATH + explected_file
    print(f'Replace {default_path} for {explected_path}')
    if (not os.path.exists(explected_path)):
        print("Replaced")
        copyfile(default_path, explected_path)
        return True
    return False


def main():
    replace_basic_file('/config/config_example.json', '/config/config.json')
    replace_basic_file('/config/config_agent_example.json', '/config/config_agent.json')
    replace_basic_file('/config/secret_key_example.txt', '/config/secret_key.txt')
    cf.info_msg("Getting current month ....", LOG_FILE)
    c_date = cf.getDatetime()
    c_date = c_date - relativedelta(months=+1)
    for day in cf.get_list_days(c_date.year, c_date.month):
        subprocess.call("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day), shell=True)
    cf.info_msg("Getting current month ....", LOG_FILE)
    c_date = cf.getDatetime()
    for day in cf.get_list_days(c_date.year, c_date.month):
        subprocess.call("{0}/src/connector_coinlayer_json.py {1}".format(PROJECT_PATH, day), shell=True)
        if cf.getDate() == day:
            break
    cf.info_msg("Current month saved ....", LOG_FILE)


if __name__ == '__main__':
    info = {
        "name": str(cf.getFiletName(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Main script for create all environment",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0]
    }
    cf.showScriptInfo(info)

    main()
