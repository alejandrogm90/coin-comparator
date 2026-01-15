from src.agents.objects.coin_movement import CoinMovement


class Bank:
    def __init__(self):
        self.list_of_movements: list[CoinMovement] = []

    def show(self):
        for cm in self.list_of_movements:
            print(cm.get_log())

    def add_movement(self, new_movement: CoinMovement) -> None:
        self.list_of_movements.append(new_movement)