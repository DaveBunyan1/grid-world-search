from grid_search.generators.grid_generator import create_random_grid
from grid_search.generators.weights_generator import assign_random_weights
from grid_search.graphs.grid import Grid
from grid_search.models.node import Node


def generate_weighted_grid(
    rows: int,
    cols: int,
    obstacle_probability: float,
    start: Node,
    goal: Node,
    min_cost: int = 1,
    max_cost: int = 10,
    seed: int | None = None,
) -> Grid:
    grid = create_random_grid(
        rows=rows,
        cols=cols,
        obstacle_probability=obstacle_probability,
        start=start,
        goal=goal,
        seed=seed,
    )

    return assign_random_weights(
        grid,
        min_cost=min_cost,
        max_cost=max_cost,
        seed=seed,
    )
