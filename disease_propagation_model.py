from typing import List
from grid import Grid
from person import Person


class DiseasePropagationModel:
    def __init__(self, grid: Grid, persons: List[Person]):
        self.grid = grid
        self.persons = persons

    def simulate_infection(self):
        for person in self.persons:
            person.execute_movement(self.grid)

    def __str__(self):
        return str(self.grid)
