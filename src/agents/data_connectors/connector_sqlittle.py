import sqlite3


class ConnectorSQLittle:
    def __init__(self, bd_path: str):
        """Constructor of ConnectorSQLittle

        :param bd_path: str
        :return: ConnectorSQLittle
        """
        self.bd_path = bd_path
        self.connect = None
        try:
            self.connect = sqlite3.connect(self.bd_path)
        except sqlite3.Error as e:
            print(e)
        if not self.connect:
            raise Exception("an error occurred while connecting to sqlittle.")
        self.cursor = self.connect.cursor()

    def get_values(self, sentence: str):
        """ Returns values from SQLite database specified by db_file

        :param sentence: sentence
        :return: Connection object or None
        """
        return self.cursor.execute(sentence).fetchall()

    def execute(self, sentence: str):
        """ Execute a command in a SQLite database specified by db_file

        :param sentence: sentence str to execute
        """
        self.cursor.execute(sentence)
        self.connect.commit()

    def exist_coin(self, date: str, name: str) -> bool:
        """Exist coin in data

        :param date: string date
        :param name: coin name
        :return: true if exist
        """
        exist_coin_sql = f"SELECT count(name) FROM coins_coin_day WHERE name = '{name}' AND date_part = '{date}' ;"
        cursor_result = self.cursor.execute(exist_coin_sql)
        if cursor_result.fetchone()[0] > 0:
            return True
        return False
