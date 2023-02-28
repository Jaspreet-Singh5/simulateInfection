from typing import Tuple
from grid import Grid


class Person:
    def __init__(self, initial_position: Tuple[int, int, str], movements: str):
        self.x = initial_position[0]
        self.y = initial_position[1]
        self.heading = initial_position[2]
        self.movements = movements

    def move_forward(self):
        if self.heading == 'N':
            self.y += 1
        elif self.heading == 'E':
            self.x += 1
        elif self.heading == 'S':
            self.y -= 1
        elif self.heading == 'W':
            self.x -= 1

    def turn_left(self):
        if self.heading == 'N':
            self.heading = 'W'
        elif self.heading == 'E':
            self.heading = 'N'
        elif self.heading == 'S':
            self.heading = 'E'
        elif self.heading == 'W':
            self.heading = 'S'

    def turn_right(self):
        if self.heading == 'N':
            self.heading = 'E'
        elif self.heading == 'E':
            self.heading = 'S'
        elif self.heading == 'S':
            self.heading = 'W'
        elif self.heading == 'W':
            self.heading = 'N'

    def execute_movement(self, grid: Grid):
        for movement in self.movements:
            if movement == 'F':
                if self.heading == 'N':
                    self.y += 1
                elif self.heading == 'E':
                    self.x += 1
                elif self.heading == 'S':
                    self.y -= 1
                elif self.heading == 'W':
                    self.x -= 1

                if self.x < 0 or self.x >= grid.length or self.y < 0 or self.y >= grid.breadth:
                    # Person moved out of grid
                    return
                if grid.cells[self.y][self.x] == 'X':
                    # Infection spreads to current cell
                    continue
                grid.cells[self.y][self.x] = 'X'

            elif movement == 'L':
                if self.heading == 'N':
                    self.heading = 'W'
                elif self.heading == 'E':
                    self.heading = 'N'
                elif self.heading == 'S':
                    self.heading = 'E'
                elif self.heading == 'W':
                    self.heading = 'S'
            elif movement == 'R':
                if self.heading == 'N':
                    self.heading = 'E'
                elif self.heading == 'E':
                    self.heading = 'S'
                elif self.heading == 'S':
                    self.heading = 'W'
                elif self.heading == 'W':
                    self.heading = 'N'
