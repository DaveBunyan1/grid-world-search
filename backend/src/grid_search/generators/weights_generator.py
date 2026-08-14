import random

from grid_search.graphs.grid import Grid
from grid_search.models.cell import Cell


def assign_random_weights(
    grid: Grid,
    min_cost: int = 1,
    max_cost: int = 10,
    seed: int | None = None,
) -> Grid:
    rng = random.Random(seed)

    cells = [
        [
            Cell(
                cost=rng.randint(min_cost, max_cost),
                blocked=cell.blocked,
            )
            for cell in row
        ]
        for row in grid.cells
    ]

    return Grid(cells)
