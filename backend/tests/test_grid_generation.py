from grid_search.generators.weighted_grid_generator import generate_weighted_grid
from grid_search.models.node import Node


def test_generate_weighted_grid_assigns_weights():
    grid = generate_weighted_grid(
        rows=10,
        cols=10,
        obstacle_probability=0.1,
        start=Node(0, 0),
        goal=Node(9, 9),
        min_cost=1,
        max_cost=10,
        seed=42,
    )

    for row in grid.cells:
        for cell in row:
            if not cell.blocked:
                assert 1 <= cell.cost <= 10


def test_generate_weighted_grid_is_reproducible():
    grid_a = generate_weighted_grid(
        rows=10,
        cols=10,
        obstacle_probability=0.1,
        start=Node(0, 0),
        goal=Node(9, 9),
        seed=42,
    )

    grid_b = generate_weighted_grid(
        rows=10,
        cols=10,
        obstacle_probability=0.1,
        start=Node(0, 0),
        goal=Node(9, 9),
        seed=42,
    )

    assert grid_a.cells == grid_b.cells
