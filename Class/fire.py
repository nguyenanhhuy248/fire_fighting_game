from game_map import *
import random


class Fire:
    def __init__(self, state):
        self.state = state
        self.power = random.choice(list(range(6, 9)))

    def display(self):
        print(
            f"Fire location: {column_list[self.state[1]]}{self.state[0]}\
            \nFire power: {self.power}"
        )
