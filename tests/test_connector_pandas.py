import unittest

from src.agents.data_connectors.connector_pandas import ConnectorPandas


class TestConnectorPandas(unittest.TestCase):
    def setUp(self):
        self.parquet_data = ConnectorPandas(["2020", "2024"],"tests/data")

    def tearDown(self):
        pass

    def test_not_empty_data(self):
        self.assertNotEqual(0, self.parquet_data.cp_df.size)
        self.assertEqual(37236, self.parquet_data.cp_df.size)

    def test_exist_coin(self):
        self.assertEqual(True, self.parquet_data.exist_coin("2020-01-01","ABC"))
        self.assertNotEqual(True, self.parquet_data.exist_coin("2020-01-03", "ABC"))



    @classmethod
    def main(cls):
        unittest.main(verbosity=2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
