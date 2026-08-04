from grid_search.algorithms.dijkstra import dijkstra
from grid_search.models.cell import Cell
from grid_search.models.grid import Grid
from grid_search.models.node import Node


def test_dijkstra_finds_low_cost_path():

    grid = Grid(
        [
            [
                Cell(cost=1),
                Cell(cost=10),
                Cell(cost=1),
            ],
            [
                Cell(blocked=True),
                Cell(cost=1),
                Cell(cost=1),
            ],
            [
                Cell(cost=1),
                Cell(cost=1),
                Cell(cost=1),
            ],
        ]
    )

    result = dijkstra(
        grid,
        Node(0, 0),
        Node(0, 2),
    )

    assert result.path is not None
