import time
import tracemalloc

from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.api.algorithm_registry import Algorithm
from grid_search.benchmarks.config import BenchmarkConfig
from grid_search.benchmarks.models import BenchmarkRecord
from grid_search.generators.grid_generator import create_random_grid
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def benchmark_search(
    algorithm: Algorithm,
    grid: Grid,
    start: Node,
    goal: Node,
    recorder: SearchEventRecorder | None = None,
) -> tuple[float, int, SearchResult]:
    tracemalloc.start()

    start_time = time.perf_counter()

    result = algorithm(grid, start, goal, recorder)

    end_time = time.perf_counter()

    _, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    runtime_ms = (end_time - start_time) * 1000

    return runtime_ms, peak_memory, result


def run_benchmark(
    config: BenchmarkConfig,
    algorithm: Algorithm,
    grid: Grid,
    start: Node,
    goal: Node,
    run: int,
) -> BenchmarkRecord:

    print(
        f"Running {algorithm.__name__} "
        f"({config.scenario}, {config.size}x{config.size}) "
        f"run {run + 1}/{config.runs}"
    )

    runtime_ms, memory_bytes, result = benchmark_search(
        algorithm,
        grid,
        start,
        goal,
    )

    return BenchmarkRecord(
        scenario=config.scenario,
        algorithm=algorithm.__name__,
        grid_size=config.size,
        obstacle_probability=config.obstacle_probability,
        run=run,
        runtime_ms=runtime_ms,
        memory_bytes=memory_bytes,
        path_found=result.path_found,
        path_length=result.path_length,
        nodes_expanded=result.nodes_expanded,
        nodes_discovered=result.nodes_discovered,
        total_cost=result.total_cost,
    )


def run_benchmark_suite(
    configs: list[BenchmarkConfig],
    algorithms: list[Algorithm],
) -> list[BenchmarkRecord]:

    records = []

    for config in configs:
        for run in range(config.runs):
            start = Node(0, 0)
            goal = Node(config.size - 1, config.size - 1)

            grid = create_random_grid(
                rows=config.size,
                cols=config.size,
                start=start,
                goal=goal,
                obstacle_probability=config.obstacle_probability,
                seed=run,
            )

            for algorithm in algorithms:
                record = run_benchmark(
                    config=config,
                    algorithm=algorithm,
                    grid=grid,
                    start=start,
                    goal=goal,
                    run=run,
                )

                records.append(record)

    return records
