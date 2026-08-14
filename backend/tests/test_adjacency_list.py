import pytest

from grid_search.algorithms.dijkstra import dijkstra
from grid_search.graphs.adjacency_list import AdjacencyListGraph
from grid_search.graphs.grid import Grid
from grid_search.models.cell import Cell
from grid_search.models.node import Node


def test_builds_adjacency_list_from_cells():
    cells = [
        [Cell(), Cell()],
        [Cell(), Cell()],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    assert graph.get_neighbours(Node(0, 0)) == [
        Node(1, 0),
        Node(0, 1),
    ]


def test_blocked_cells_are_excluded():
    cells = [
        [Cell(), Cell(blocked=True)],
        [Cell(), Cell()],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    assert graph.get_neighbours(Node(0, 0)) == [
        Node(1, 0),
    ]


def test_blocked_cell_is_not_a_node():
    cells = [
        [Cell(), Cell(blocked=True)],
        [Cell(), Cell()],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    assert graph.get_neighbours(Node(0, 1)) == []


def test_get_edge_cost_uses_destination_cell_cost():
    cells = [
        [Cell(cost=1), Cell(cost=5)],
        [Cell(cost=3), Cell(cost=7)],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    assert (
        graph.get_edge_cost(
            Node(0, 0),
            Node(0, 1),
        )
        == 5
    )

    assert (
        graph.get_edge_cost(
            Node(0, 0),
            Node(1, 0),
        )
        == 3
    )


def test_edge_cost_depends_on_destination():
    cells = [
        [Cell(cost=2), Cell(cost=8)],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    assert (
        graph.get_edge_cost(
            Node(0, 0),
            Node(0, 1),
        )
        == 8
    )

    assert (
        graph.get_edge_cost(
            Node(0, 1),
            Node(0, 0),
        )
        == 2
    )


def test_get_edge_cost_raises_for_nonexistent_edge():
    cells = [
        [Cell(), Cell(blocked=True)],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    with pytest.raises(ValueError):
        graph.get_edge_cost(
            Node(0, 0),
            Node(0, 1),
        )


def test_dijkstra_works_with_adjacency_list():
    cells = [
        [Cell(), Cell(cost=10), Cell()],
        [Cell(), Cell(cost=1), Cell()],
        [Cell(), Cell(), Cell()],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    result = dijkstra(
        graph,
        Node(0, 0),
        Node(0, 2),
    )

    assert result.path_found is True


def test_dijkstra_finds_low_cost_path():
    cells = [
        [Cell(cost=1), Cell(cost=10), Cell(cost=1)],
        [Cell(cost=1), Cell(cost=1), Cell(cost=1)],
    ]

    graph = AdjacencyListGraph.from_cells(cells)

    result = dijkstra(
        graph,
        Node(0, 0),
        Node(0, 2),
    )

    assert result.path_found is True
    assert result.total_cost == 4


def test_adjacency_list_matches_grid():
    cells = [
        [Cell(), Cell(cost=5), Cell()],
        [Cell(blocked=True), Cell(cost=2), Cell()],
    ]

    grid = Grid(cells)
    graph = AdjacencyListGraph.from_cells(cells)

    nodes = [
        Node(0, 0),
        Node(0, 1),
        Node(0, 2),
        Node(1, 1),
        Node(1, 2),
    ]

    for node in nodes:
        assert grid.get_neighbours(node) == graph.get_neighbours(node)

        for neighbour in grid.get_neighbours(node):
            assert grid.get_edge_cost(node, neighbour) == (
                graph.get_edge_cost(node, neighbour)
            )
