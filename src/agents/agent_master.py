import sys
import pandas

from src.agents.common_utils import CommonFunctions
from src.agents.data_connectors.connector_sqlittle import ConnectorSQLittle
from src.agents.objects.coin_movement import CoinMovement


def get_price_sql(config: dict, date: str, name: str) -> float | None:
    con1 = ConnectorSQLittle(config['SQL_PATH'])
    sentence = "SELECT value FROM coins_coin_day WHERE date_part <= "
    sentence += f"'{date}' AND name='{name}' ORDER BY date_part DESC LIMIT 1"
    rows = con1.get_values(sentence)
    if len(rows) > 0:
        return float(rows[0][0])
    return None

def get_price_parquet(config: dict, date: str, name: str) -> float | None:
    try:
        # Carga el archivo Parquet en un DataFrame de pandas
        df = pandas.read_parquet(config['PARQUET_PATH'])

        # Filtra el DataFrame por la fecha y el nombre del activo
        filtered_df = df[(df['date'] <= date) & (df['name'] == name)]

        # Si no hay filas que cumplan con las condiciones, devuelve None
        if filtered_df.empty:
            return None

        # Ordena el DataFrame por fecha en orden descendente y toma la primera fila
        latest_row = filtered_df.sort_values(by='date', ascending=False).head(1)

        # Devuelve el precio como float
        return float(latest_row['value'].iloc[0])
    except FileNotFoundError:
        print(f"El archivo {config['PARQUET_PATH']} no existe")
    except pandas.errors.EmptyDataError:
        print(f"El archivo {config['PARQUET_PATH']} está vacío")
    except Exception as e:
        print(f"Error al leer el archivo Parquet: {e}")
    return None



class AgentMaster:
    def __init__(self, log_file: str):
        self.log_file = log_file
        self.config = CommonFunctions.load_config(log_file=self.log_file)
        self.config_agent = CommonFunctions.load_json(sys.argv[1])

        my_bank = CoinMovement(self.config_agent, sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]),
        # get_price_sql(self.config, sys.argv[2], sys.argv[3]))
        get_price_parquet(self.config, sys.argv[2], sys.argv[3]))
        my_bank.show()
