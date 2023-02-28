from typing import List, Tuple


class Grid:
    def __init__(self, length: int, breadth: int, infected_cells: List[Tuple[int, int]]):
        self.length = length
        self.breadth = breadth
        self.cells = [['O' for _ in range(breadth)] for _ in range(length)]
        self.infect_cells(infected_cells)

    def infect_cells(self, infected_cells: List[Tuple[int, int]]):
        for cell in infected_cells:
            self.cells[cell[0]][cell[1]] = 'X'

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.cells])
