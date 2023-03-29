import tkinter as tk
from environment import *
from config import *


class EnvironmentGUI(tk.Canvas, Environment):
    def __init__(self, master, environment, size=PIXEL_SIZE, interval=REFRESH_TIME):
        self.environment = environment
        self.rows = len(environment.board[0])
        self.cols = len(environment.board)
        self.size = size

        super().__init__(master, width=self.cols * size, height=self.rows * size)

        self.interval = interval
        self.new_colors = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        self.color_board = environment.color_board
        self.pixel_ids = []
        self.display_gui_board()
        self.update_gui_board()

    def display_gui_board(self):
        for y in range(self.rows):
            row_pixels = []
            for x in range(self.cols):
                start_point = [x * self.size, y * self.size]
                end_point = [start_point[0] + self.size, start_point[1] + self.size]
                pixel_id = self.create_rectangle(start_point[0], start_point[1], end_point[0], end_point[1],
                                                 fill=self.new_colors[y][x], outline="")
                row_pixels.append(pixel_id)
            self.pixel_ids.append(row_pixels)

    def update_gui_board(self):
        self.environment.update_color_map()
        for y in range(self.rows):
            for x in range(self.cols):
                self.new_colors[y][x] = self.color_board[y][x]
        self.update_pixels()
        self.after(self.interval, self.update_gui_board)

    def update_pixels(self):
        for y in range(self.rows):
            for x in range(self.cols):
                self.itemconfig(self.pixel_ids[y][x], fill=self.new_colors[y][x], outline="")
