class Coin:
    def __init__(self, name: str='', current_date: str='', current_price: float=0):
        self.name: str = name
        self.current_date: str = current_date
        self.current_price: float = float(current_price)

    def __str__(self):
        return f'{self.name}|{self.current_date}|{self.current_price}'

    def __dict__(self):
        return {
            "name": self.name,
            "current_date": self.current_date,
            "current_price": self.current_price
        }

    def get_log(self):
        return str(self)


if __name__ == '__main__':
    print("class CoinMovement")
