import os
import sys
import pandas

from src.agents.common_utils import CommonFunctions

# GLOBALS
PROJECT_PATH = CommonFunctions.get_project_path()
LOG_FILE = PROJECT_PATH + "/log/" + CommonFunctions.get_file_log(sys.argv[0])
CONFIG = CommonFunctions.load_config(f"{PROJECT_PATH}/config/config.json", LOG_FILE)

if __name__ == '__main__':
    info = {
        "name": str(CommonFunctions.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Create a complete data file of a year in CSV and JSON",
        "author": "Alejandro Gómez",
        "parameters": [f"{sys.argv[0]} 2023"]
    }
    CommonFunctions.show_script_info(info)

    # Constants
    DATA_DIRECTORY = PROJECT_PATH + "/data/json/"
    OUTPUT_DIRECTORY = PROJECT_PATH + "/data/dataFrames/"
    CURRENT_YEAR = ""
    MY_COLUMNS = ["date", "name", "value"]
    df_pandas = pandas.DataFrame(columns=MY_COLUMNS)

    if len(sys.argv) != 2:
        CommonFunctions.error_msg_parameters(info, LOG_FILE)
    else:
        CURRENT_YEAR = sys.argv[1]
        DATA_DIRECTORY = f"{DATA_DIRECTORY}{CURRENT_YEAR}/"

    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    if not os.path.exists(DATA_DIRECTORY):
        CommonFunctions.error_msg(2, DATA_DIRECTORY + " directory do not exist", LOG_FILE)
    else:
        print(f"Loading data from path: {DATA_DIRECTORY}")
        for root, dirs, files in os.walk(DATA_DIRECTORY):
            for name in files:
                if name.endswith('.json'):
                    file_path = os.path.join(root, name)
                    CommonFunctions.info_msg(f"Loading file: {file_path}")
                    data = CommonFunctions.load_json(file_path)
                    # For each value in a day
                    for element in data["rates"]:
                        df_pandas.loc[len(df_pandas)] = [data["date"], element, data["rates"][element]]
        # Write data to output file
        OUTPUT_NAME = f'FULL_COPY_{CURRENT_YEAR}'
        OUTPUT_PATH = OUTPUT_DIRECTORY + OUTPUT_NAME

        #df_pandas.to_csv(f"{OUTPUT_PATH}.csv", index=False)
        #df_pandas.to_json(f"{OUTPUT_PATH}.json")
        #df_pandas.to_excel(f"{OUTPUT_PATH}.xlsx")
        parquet_base_name = f"{OUTPUT_PATH}.parquet"
        print(f'OUTPUT_PATH: {OUTPUT_PATH}')
        if not os.path.exists(parquet_base_name) or not os.path.isdir(parquet_base_name):
            os.makedirs(parquet_base_name)
        df_pandas.to_parquet(parquet_base_name, engine='pyarrow', compression='gzip', partition_cols=['date'])
        CommonFunctions.info_msg(OUTPUT_NAME + " has been saved.", LOG_FILE)
