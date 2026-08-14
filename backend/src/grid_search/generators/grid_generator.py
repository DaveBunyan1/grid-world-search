import random

from grid_search.graphs.grid import Grid
from grid_search.models.cell import Cell
from grid_search.models.node import Node


def create_random_grid(
    rows: int,
    cols: int,
    start: Node,
    goal: Node,
    obstacle_probability: float = 0.2,
    seed: int | None = None,
) -> Grid:
    if not (0 <= start.row < rows and 0 <= start.col < cols):
        raise ValueError("Start node is outside grid")

    if not (0 <= goal.row < rows and 0 <= goal.col < cols):
        raise ValueError("Goal node is outside grid")

    if seed is not None:
        random.seed(seed)

    cells = []

    for row in range(rows):
        current_row = []

        for col in range(cols):
            if (row, col) == (start.row, start.col):
                current_row.append(Cell())

            elif (row, col) == (goal.row, goal.col):
                current_row.append(Cell())

            elif random.random() < obstacle_probability:
                current_row.append(Cell(blocked=True))

            else:
                current_row.append(Cell())

        cells.append(current_row)

    return Grid(cells)
