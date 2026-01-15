import os.path
import sys
import requests

from src.agents.common_utils import CommonFunctions

# Example: pipenv run python src/connector_coinlayer_json.py "2024-01-31"

# GLOBALS
LOG_FILE = "log/" + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(log_file=LOG_FILE)


def save_day_in_json(selected_date):
    selected_year = selected_date.split('-')[0]
    selected_month = selected_date.split('-')[1]
    json_path = f"data/json/{selected_year}/{selected_month}/{selected_date}_coinlayer.json"
    if not os.path.exists(json_path):
        host_url = CONFIG["HOST_URL"]
        access_key = CONFIG["ACCESS_KEY"]
        url_1 = f'{host_url}/{selected_date}?access_key={access_key}'

        payload = {}
        headers = {}
        response = requests.request("GET", url_1, headers=headers, data=payload)
        data = response.json()
        # print(data)
        CommonFunctions.save_json(json_path, data)
        CommonFunctions.info_msg("DATA SAVED IN: {0}".format(json_path), LOG_FILE)
    else:
        CommonFunctions.info_msg("FILE ALREADY EXISTS IN: {0}".format(json_path), LOG_FILE)


if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        CommonFunctions.error_msg(1, "Erroneous parameter number.", LOG_FILE)

    save_day_in_json(str(sys.argv[1]))
