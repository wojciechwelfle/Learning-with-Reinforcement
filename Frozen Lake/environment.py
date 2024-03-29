from direction import *
from config import *


class Environment:
    def __init__(self):
        self.minPosX = 0
        self.maxPosX = WIDTH - 1
        self.minPosY = 0
        self.maxPosY = HEIGHT - 1

        self.start = 0

        self.pos_x = self.start
        self.pos_y = self.start
        self.accepting_state = ACCEPTING_STATES
        self.color_board = [["#ffffff" for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.end_state = END_STATE
        self.penalty = PENALTY
        self.penalty_value = PENALTY_VALUE

        self.board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.board[END_STATE[0]][END_STATE[1]] = 1
        # self.set_penalty()

        self.new_colors = {
            "yellow": "#FFC300",
            "green": "#32CD32",
            "blue": "#89CFF0",
            "brown": "#6E260E",
            "red": "#D2042D"
        }

    def step(self, action):
        if action == LEFT and self.pos_x != self.minPosX:
            self.pos_x -= 1
        if action == RIGHT and self.pos_x != self.maxPosX:
            self.pos_x += 1
        if action == UP and self.pos_y != self.minPosY:
            self.pos_y -= 1
        if action == DOWN and self.pos_y != self.maxPosY:
            self.pos_y += 1
        return [self.pos_x, self.pos_y]

    def set_to_initial_pos(self):
        self.pos_x = self.start
        self.pos_y = self.start

    def get_reward(self):
        x = self.pos_x
        y = self.pos_y
        return self.board[x][y]

    def get_position_x(self):
        return self.pos_x

    def get_position_y(self):
        return self.pos_y

    def get_position(self):
        return [self.pos_x, self.pos_y]

    def is_end_position(self):
        for i in range(len(self.accepting_state)):
            x = self.accepting_state[i][0]
            y = self.accepting_state[i][1]
            if x == self.pos_x and y == self.pos_y:
                return True
        if self.pos_x == self.end_state[0] and self.pos_y == self.end_state[1]:
            return True
        return False

    def is_end_position_xy(self, p_x, p_y):
        for i in range(len(self.accepting_state)):
            x = self.accepting_state[i][0]
            y = self.accepting_state[i][1]
            if x == p_x and y == p_y:
                return True
        if p_x == self.end_state[0] and p_y == self.end_state[1]:
            return True
        return False

    def display_board(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if x == self.pos_x and y == self.pos_y:
                    print("P", end="")
                elif x == self.end_state[0] and y == self.end_state[1]:
                    print("E", end="")
                elif self.is_end_position_xy(x, y):
                    print("H", end="")
                else:
                    print("_", end="")
            print()
        print()

    def update_color_map(self):
        for y in range(len(self.color_board)):
            for x in range(len(self.color_board[0])):
                if x == self.pos_x and y == self.pos_y:
                    self.color_board[y][x] = self.new_colors["red"]
                elif x == self.start and y == self.start:
                    self.color_board[y][x] = self.new_colors["yellow"]
                elif x == self.end_state[0] and y == self.end_state[1]:
                    self.color_board[y][x] = self.new_colors["green"]
                elif self.is_end_position_xy(x, y):
                    self.color_board[y][x] = self.new_colors["brown"]
                else:
                    self.color_board[y][x] = self.new_colors["blue"]

    def set_penalty(self):
        for penalties in self.penalty:
            self.board[penalties[0]][penalties[1]] = self.penalty_value
