import os.path
import sys

import requests

from src.utils.common_functions import error_msg, get_file_log, info_msg, load_config, save_json

# GLOBALS
LOG_FILE = "log/" + get_file_log(sys.argv[0])
CONFIG = load_config(log_file=LOG_FILE)


def save_day_in_json(selected_date):
    selected_year = selected_date.split('-')[0]
    json_path = "data/" + selected_year + "/" + selected_date + "_coinlayer.json"
    if not os.path.exists(json_path):
        host_url = CONFIG["HOST_URL"]
        access_key = CONFIG["ACCESS_KEY"]
        url_1 = f'{host_url}/{selected_date}?access_key={access_key}'

        payload = {}
        headers = {}
        response = requests.request("GET", url_1, headers=headers, data=payload)
        data = response.json()
        print(data)
        save_json(json_path, data)
        info_msg("DATA SAVED IN: {0}".format(json_path), LOG_FILE)
    else:
        info_msg("FILE ALREADY EXISTS IN: {0}".format(json_path), LOG_FILE)


if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        error_msg(1, "Erroneous parameter number.", LOG_FILE)

    save_day_in_json(str(sys.argv[1]))
