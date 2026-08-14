from grid_search.algorithms.astar import astar
from grid_search.algorithms.dijkstra import dijkstra
from grid_search.graphs.grid import Grid
from grid_search.models.cell import Cell
from grid_search.models.node import Node


def test_astar_finds_low_cost_path():

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

    result = astar(
        grid,
        Node(0, 0),
        Node(0, 2),
    )

    assert result.path is not None
    assert result.total_cost is not None

    dijkstra_result = dijkstra(grid, Node(0, 0), Node(0, 2))

    assert result.total_cost == dijkstra_result.total_cost
