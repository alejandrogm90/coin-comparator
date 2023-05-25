from django.test import TestCase
from .models import coin_day


class coinDayTest(TestCase):
    def test_object(self):
        """
        test coin_day
        """
        cd = coin_day('2023-01-01_BTC', '2023-01-01', 'BTC', 2.12321)
        self.assertIs(cd.id, '2023-01-01_BTC')
        self.assertIs(cd.date_part, '2023-01-01')
        self.assertIs(cd.name, 'BTC')
        self.assertIs(cd.value, 2.12321)
