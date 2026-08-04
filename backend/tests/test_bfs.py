from grid_search.algorithms.bfs import bfs
from grid_search.grid import Grid
from grid_search.models.node import Node


def test_bfs_finds_path():

    grid = Grid(
        [
            ["S", ".", "."],
            ["#", "#", "."],
            [".", ".", "G"],
        ]
    )

    path = bfs(grid, Node(0, 0), Node(2, 2))

    assert path is not None

    assert path[0] == Node(0, 0)
    assert path[-1] == Node(2, 2)
