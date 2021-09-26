import random
import numpy as np
from result_handler import check_result, save_game_state


class GameField:
    def __init__(self, width=5, height=5, mines_count=random.randint(2, 5)):
        self.width = width
        self.height = height
        self.mines_count = mines_count
        self.field = [["." for _ in range(width)] for _ in range(height)]
        self.filled_playing_field = [[0 for _ in range(width)] for _ in range(height)]
        self.opened_cells_count = 0
        self.correctly_marked_mines_count = 0
        self.first_step_flag = True

    def placed_mines(self, start_x, start_y):
        placed_mines_count = 0
        while placed_mines_count != self.mines_count:
            cell = {'x': np.random.randint(0, self.width - 1),
                    'y': np.random.randint(0, self.height - 1)}
            if (cell['x'] != start_x or cell['y'] != start_y) and \
                    self.filled_playing_field[cell['y']][cell['x']] != "*":
                self.filled_playing_field[cell['y']][cell['x']] = "*"
                placed_mines_count += 1

    def fill_playing_field(self, start_x, start_y):
        self.placed_mines(start_x, start_y)
        for x in range(self.width):
            for y in range(self.height):
                if self.filled_playing_field[y][x] == "*":
                    continue
                mines_count = 0
                for x_shift in range(-1, 2):
                    for y_shift in range(-1, 2):
                        row_index = y + y_shift
                        column_index = x + x_shift
                        if row_index < 0 or row_index >= self.height \
                                or column_index < 0 or column_index >= self.width:
                            continue
                        if self.filled_playing_field[row_index][column_index] == "*":
                            mines_count += 1
                self.filled_playing_field[y][x] = mines_count

    def set_flag(self, x, y):
        self.field[y][x] = "f"
        if self.filled_playing_field[y][x] == "*":
            self.correctly_marked_mines_count += 1
        if self.correctly_marked_mines_count == self.mines_count:
            self.field = self.filled_playing_field
            save_game_state(self.filled_playing_field)
            check_result(True, self.opened_cells_count)

    def open_cell(self, x, y):
        if self.field[y][x] == ".":
            self.opened_cells_count += 1
        if self.first_step_flag:
            self.first_step_flag = False
            self.fill_playing_field(x, y)
        if self.filled_playing_field[y][x] == "*":
            self.field = self.filled_playing_field
            save_game_state(self.filled_playing_field)
            check_result(False, self.opened_cells_count)
        else:
            self.field[y][x] = self.filled_playing_field[y][x]
            if self.field[y][x] == 0:
                self.open_neighbors(x, y)
            if self.opened_cells_count == self.width * self.height - self.mines_count:
                # save_game_state(self.filled_playing_field)
                self.field = self.filled_playing_field
                check_result(True, self.opened_cells_count)

    def open_neighbors(self, x, y):
        for x_shift in range(-1, 2):
            for y_shift in range(-1, 2):
                if x_shift == 0 and y_shift == 0:
                    continue
                row_index = y + y_shift
                column_index = x + x_shift
                if row_index < 0 or row_index >= self.height \
                        or column_index < 0 or column_index >= self.width:
                    continue
                if self.filled_playing_field[row_index][column_index] != "*":
                    if self.field[row_index][column_index] == ".":
                        self.opened_cells_count += 1
                    self.field[row_index][column_index] = self.filled_playing_field[row_index][column_index]
