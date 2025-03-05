import sqlite3


class ConnectorSQLittle:
    def __init__(self, bd_path: str):
        """

        :param bd_path: str
        :return: ConnectorSQLittle
        """
        self.bd_path = bd_path
        self.connect = None
        try:
            self.connect = sqlite3.connect(self.bd_path)
        except sqlite3.Error as e:
            print(e)
        except Exception as e:
            print(e)
        if not self.connect:
            raise Exception("an error occurred while connecting to sqlittle.")
        self.cursor = self.connect.cursor()

    def get_values(self, sentence: str):
        """ Returns values from SQLite database specified by db_file

        :param sentence: sentence
        :return: Connection object or None
        """
        rows = ""
        try:
            rows = self.cursor.execute(sentence).fetchall()
        except sqlite3.Error as e:
            print(e)
        return rows

    def execute(self, sentence: str):
        """ Execute a command in a SQLite database specified by db_file

        :param sentence: sentence str to execute
        """
        try:
            self.cursor.execute(sentence)
            self.connect.commit()
        except sqlite3.Error as e:
            print(e)

    def exist_coin(self, sdate: str, name: str) -> bool:
        """Exist coin in data

        :param sdate: string date
        :param name: coin name
        :return: true if exist
        """
        sql = f"SELECT count(name) FROM coins_coin_day WHERE name = '{name}' AND date_part = '{sdate}' ;"
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except sqlite3.Error as e:
            print(e)
        if self.cursor.fetchone()[0] > 0:
            return True
        else:
            return False
