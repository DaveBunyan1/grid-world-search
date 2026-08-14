from grid_search.algorithms.dfs import dfs
from grid_search.graphs.grid import Grid
from grid_search.models.cell import Cell
from grid_search.models.node import Node


def test_dfs_finds_path():

    grid = Grid(
        [
            [
                Cell(),
                Cell(),
                Cell(),
            ],
            [
                Cell(blocked=True),
                Cell(blocked=True),
                Cell(),
            ],
            [
                Cell(),
                Cell(),
                Cell(),
            ],
        ]
    )

    result = dfs(
        grid,
        Node(0, 0),
        Node(2, 2),
    )

    assert result.path is not None

    assert result.path[0] == Node(0, 0)
    assert result.path[-1] == Node(2, 2)


def test_dfs_tracks_search_metrics():

    grid = Grid(
        [
            [
                Cell(),
                Cell(),
                Cell(),
            ],
            [
                Cell(blocked=True),
                Cell(blocked=True),
                Cell(),
            ],
            [
                Cell(),
                Cell(),
                Cell(),
            ],
        ]
    )

    result = dfs(
        grid,
        Node(0, 0),
        Node(2, 2),
    )

    assert result.nodes_expanded > 0
    assert result.nodes_discovered >= result.nodes_expanded


def test_dfs_returns_none_when_no_path():

    grid = Grid(
        [
            [
                Cell(),
                Cell(),
                Cell(),
            ],
            [
                Cell(blocked=True),
                Cell(blocked=True),
                Cell(blocked=True),
            ],
            [
                Cell(),
                Cell(),
                Cell(),
            ],
        ]
    )

    result = dfs(
        grid,
        Node(0, 0),
        Node(2, 2),
    )

    assert result.path is None
