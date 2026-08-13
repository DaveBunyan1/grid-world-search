from grid_search.api.algorithm_registry import ALGORITHMS
from grid_search.benchmarks.runner import benchmark_search
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def compare_algorithms(
    grid: Grid,
    start: Node,
    goal: Node,
) -> dict[str, tuple[float, int, SearchResult]]:
    results = {}

    for name, algorithm in ALGORITHMS.items():
        runtime_ms, memory_bytes, result = benchmark_search(
            algorithm,
            grid,
            start,
            goal,
        )

        results[name] = (
            runtime_ms,
            memory_bytes,
            result,
        )

    return results
