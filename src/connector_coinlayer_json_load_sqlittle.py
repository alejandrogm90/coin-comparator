import os
import sys

from src.common_utils.common_functions import CommonFunctions
from src.common_utils.connector_sqlittle import ConnectorSQLittle

# GLOBALS
LOG_FILE = "log/" + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(log_file=LOG_FILE)

if __name__ == '__main__':
    # PARAMETERS
    if len(sys.argv) != 2:
        CommonFunctions.error_msg(1, "Erroneous parameter number.", LOG_FILE)

    selected_date = str(sys.argv[1])
    selected_year = selected_date.split('-')[0]
    json_path = f"data/json/{selected_year}/{selected_date}_coinlayer.json"
    # Cargar datos desde los ficheros JSON previamente generados
    if os.path.exists(json_path):
        con1 = ConnectorSQLittle(CONFIG["SQLITLE_PATH"])
        data = CommonFunctions.load_json(json_path)
        first_part = "INSERT INTO coins_coin_day (id, date_part, name, value)"
        for element in data["rates"]:
            sentence = f"{first_part} VALUES('{selected_date}_{element}', '{selected_date}, '{element}', "
            sentence += f"{str(data['rates'][element])})"
            con1.execute(sentence)
    else:
        CommonFunctions.error_msg(2, json_path + " file do not exist", LOG_FILE)
