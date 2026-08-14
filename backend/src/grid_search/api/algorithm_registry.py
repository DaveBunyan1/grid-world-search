from collections.abc import Callable

from grid_search.algorithms.bfs import bfs
from grid_search.algorithms.dfs import dfs
from grid_search.algorithms.weighted_algorithms import astar, dijkstra
from grid_search.models.search_result import SearchResult

Algorithm = Callable[
    ...,
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
