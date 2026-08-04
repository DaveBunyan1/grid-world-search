from grid_search.algorithms.astar import astar
from grid_search.algorithms.bfs import bfs
from grid_search.algorithms.dfs import dfs
from grid_search.algorithms.dijkstra import dijkstra
from grid_search.benchmarks.config import BENCHMARKS
from grid_search.benchmarks.exporter import export_csv
from grid_search.benchmarks.runner import run_benchmark_suite


def main():
    algorithms = [
        bfs,
        dfs,
        dijkstra,
        astar,
    ]

    records = run_benchmark_suite(
        BENCHMARKS,
        algorithms,
    )

    export_csv(
        records,
        "benchmark_results.csv",
    )


if __name__ == "__main__":
    main()
