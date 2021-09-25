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
        self.correctly_marked_cells_count = 0

    def placed_mines(self, start_x=None, start_y=None):
        placed_mines_count = 0
        while placed_mines_count != self.mines_count:
            point = {'x': np.random.randint(0, self.width - 1),
                     'y': np.random.randint(0, self.height - 1)}
            if point['x'] != start_x and point != start_y and \
                    self.filled_playing_field[-point['y']][point['x']] != "*":
                self.filled_playing_field[-point['y']][point['x']] = "*"
                placed_mines_count += 1

    def fill_playing_field(self, start_x=None, start_y=None):
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
        self.field[self.height - y][x - 1] = "f"
        if self.filled_playing_field[self.height - y][x - 1] == "*":
            self.correctly_marked_cells_count += 1
        if self.correctly_marked_cells_count == len(self.filled_playing_field):
            # save_game_state(self.filled_playing_field)
            check_result(True)

    def open_cell(self, x, y):
        self.opened_cells_count += 1
        if self.filled_playing_field[self.height - y][x - 1] == "*":
            self.field = self.filled_playing_field
            # save_game_state(self.filled_playing_field)
            check_result(False)
        else:
            self.field[self.height - y][x - 1] = self.filled_playing_field[self.height - y][x - 1]
            # if self.field[self.height - y][x - 1] == 0:
            #     self.open_neighbors(x-1, self.height - y)
            if self.opened_cells_count == self.width * self.height - self.mines_count:
                # save_game_state(self.filled_playing_field)
                check_result(True)

    # def open_neighbors(self, x, y):
    #     self.field[y][x] = 0
    #     for x_shift in range(-1, 2):
    #         for y_shift in range(-1, 2):
    #             if x_shift == 0 and y_shift == 0:
    #                 continue
    #             row_index = self.height - y + y_shift
    #             column_index = x + x_shift
    #             if row_index < 0 or row_index >= self.height \
    #                     or column_index < 0 or column_index >= self.width:
    #                 continue
    #             if self.mines_matrix[row_index][column_index] == 0:
    #                 self.open_neighbors(column_index, row_index)
