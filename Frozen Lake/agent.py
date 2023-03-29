import random
from direction import *


class Agent:
    def __init__(self):
        self._alpha = 0.1
        self._gamma = 0.9
        self._epsilon = 0.9
        self.qTable = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]

    def get_best_action(self, pos_x, pos_y):
        direction = []
        best_action_idx = 0
        for dirs in range(4):
            direction.append(self.qTable[pos_x][pos_y][dirs])
            if direction[dirs] > self.qTable[pos_x][pos_y][best_action_idx]:
                best_action_idx = dirs
        zero = 0
        for elem in direction:
            if elem <= 0.0001:
                zero += 1
        if zero == 4:
            return random.randrange(4)
        return best_action_idx

    def get_action(self, pos_x, pos_y):
        if random.random() <= self._epsilon:
            return random.randrange(4)
        return self.get_best_action(pos_x, pos_y)

    def update(self, pos_x, pos_y, action, reward, new_pos_x, new_pos_y, is_done):
        a = self._alpha
        g = self._gamma
        if is_done:
            self.qTable[pos_x][pos_y][action] += a * (reward - self.qTable[pos_x][pos_y][action])
        else:
            best_action = self.get_best_action(new_pos_x, new_pos_y)
            self.qTable[pos_x][pos_y][action] += a * (
                    reward + g * self.qTable[new_pos_x][new_pos_y][best_action] - self.qTable[pos_x][pos_y][action])

    def display_states(self):
        for y in range(4):
            for x in range(4):
                print(f"State: {x, y} ", end="")
                print(f"Left: {self.qTable[y][x][LEFT]:.4f} ", end="")
                print(f"Right: {self.qTable[y][x][RIGHT]:.4f} ", end="")
                print(f"UP: {self.qTable[y][x][UP]:.4f} ", end="")
                print(f"DOWN: {self.qTable[y][x][DOWN]:.4f} ", end="")
                print()
