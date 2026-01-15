import glob
import sys
import pandas

from src.agents.common_utils import CommonFunctions

# GLOBALS
LOG_FILE = "log/" + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(log_file=LOG_FILE)

if __name__ == '__main__':
    columns_df = ["date_part", "name", "value"]
    current_df = pandas.DataFrame(columns=columns_df)

    path_to_json = 'data/2020'
    json_files = glob.glob(path_to_json + '/**/*.json', recursive=True)

    print(f"json_files: {json_files}")
    # Cargar datos desde los ficheros JSON previamente generados
    for json_path in json_files:
        print(f"Loading: {json_path}")
        data = CommonFunctions.load_json(json_path)
        if "rates" in data:
            for element in data["rates"]:
                current_df.loc[len(current_df)] = [data["date"], element, data["date"][element]]

    current_df.to_csv('AA_test.csv')
