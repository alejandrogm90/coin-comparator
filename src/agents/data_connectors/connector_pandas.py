import pandas


class ConnectorPandas:
    def __init__(self, years: list[str], folder_path: str="data/dataFrames"):
        """Constructor of ConnectorSQLittle

        :param years: list of string example ("2024","2025")
        :param folder_path: folder path by default "data/dataFrames/"
        :return: ConnectorSQLittle
        """
        self.cp_df = pandas.DataFrame()
        for year in years:
            self.cp_df = self.cp_df._append(pandas.read_parquet(f"{folder_path}/FULL_COPY_{year}.parquet"))

        self.cp_df['date'] = self.cp_df['date'].astype(object)
        self.cp_df['date'] = pandas.to_datetime(self.cp_df['date'])

    def exist_coin(self, date: str, name: str) -> bool:
        """Exist coin in data

        :param date: string date
        :param name: coin name
        :return: true if exist
        """
        question_result = self.cp_df.query(f"name=='{name}' and date=='{date}' ")
        if question_result.size > 0:
            return True
        return False

    def get_values(self, sentence: str):
        """ Returns values from SQLite database specified by db_file

        :param sentence: sentence
        :return: Connection object or None
        """
        print(f"count: {self.cp_df.size}")
        print(sentence)
        #return self.cp_df.query(sentence, inplace=True)
        return self.cp_df.query(sentence)

    def get_data_frame(self) -> pandas.DataFrame:
        """ Returns full pandas.DataFrame

        :return: a pandas.DataFrame
        """
        return self.cp_df
