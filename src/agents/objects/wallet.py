from src.agents.objects.action import Movement
from src.agents.objects.coin_movement import ActionType


class Wallet:
    def __init__(self):
        self.cash = float(0)
        self.movements = []

    def is_valid_movement(self, movement: Movement):
        if movement.action == ActionType.BUY:
            if (self.cash - movement.total_price()) < 0:
                return False
        return True

    def make_movement(self, movement: Movement):
        if self.is_valid_movement(movement):
            self.movements.append(movement)


if __name__ == '__main__':
    print("class Wallet")
