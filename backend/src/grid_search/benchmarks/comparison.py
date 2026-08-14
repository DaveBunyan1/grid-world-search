from grid_search.api.algorithm_registry import ALGORITHMS
from grid_search.api.schemas import RepresentationMetrics
from grid_search.benchmarks.runner import benchmark_search
from grid_search.graphs.adjacency_list import AdjacencyListGraph
from grid_search.graphs.adjacency_list_cost_map import AdjacencyListWithCostMap
from grid_search.graphs.adjacency_matrix import AdjacencyMatrix
from grid_search.graphs.csr import CSR
from grid_search.graphs.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def compare_algorithms(
    grid: Grid,
    start: Node,
    goal: Node,
) -> dict[str, tuple[SearchResult, list[RepresentationMetrics]]]:

    representations = {
        "grid": grid,
        "adjacency_list": AdjacencyListGraph.from_cells(grid.cells),
        "adjacency_list_cm": AdjacencyListWithCostMap.from_cells(grid.cells),
        "csr": CSR.from_cells(grid.cells),
        "adjacency_matrix": AdjacencyMatrix.from_cells(grid.cells),
    }
    results = {}

    for algorithm_name, algorithm in ALGORITHMS.items():
        representation_results = []

        search_result = None

        for representation_name, graph in representations.items():
            runtime_ms, memory_bytes, result = benchmark_search(
                algorithm,
                graph,
                start,
                goal,
            )

            representation_results.append(
                RepresentationMetrics(
                    representation=representation_name,
                    runtime_ms=runtime_ms,
                    memory_bytes=memory_bytes,
                )
            )

            if search_result is None:
                search_result = result

        results[algorithm_name] = (
            search_result,
            representation_results,
        )

    return results
