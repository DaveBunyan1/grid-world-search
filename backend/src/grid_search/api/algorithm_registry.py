from collections.abc import Callable

from grid_search.algorithms.astar import astar
from grid_search.algorithms.bfs import bfs
from grid_search.algorithms.dfs import dfs
from grid_search.algorithms.dijkstra import dijkstra
from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.graphs.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult

Algorithm = Callable[
    [Grid, Node, Node, SearchEventRecorder | None],
    SearchResult,
]


ALGORITHMS: dict[str, Algorithm] = {
    "bfs": bfs,
    "dfs": dfs,
    "dijkstra": dijkstra,
    "astar": astar,
}


def get_algorithm(name: str) -> Algorithm:
    try:
        return ALGORITHMS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown algorithm: {name}") from exc


def get_algorithm_names() -> list[str]:
    return list(ALGORITHMS.keys())
