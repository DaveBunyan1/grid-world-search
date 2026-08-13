from fastapi import APIRouter

from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.api.algorithm_registry import get_algorithm, get_algorithm_names
from grid_search.api.mappers import (
    grid_from_schema,
    grid_to_schema,
    node_from_schema,
    search_result_to_schema,
)
from grid_search.api.schemas import (
    AlgorithmComparisonResult,
    BenchmarkResponse,
    ComparisonRequest,
    ComparisonResponse,
    GenerateGridRequest,
    GenerateGridResponse,
    SearchRequest,
)
from grid_search.benchmarks.comparison import compare_algorithms
from grid_search.benchmarks.runner import benchmark_search
from grid_search.generators.grid_generator import create_random_grid
from grid_search.models.node import Node

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/algorithms", response_model=list[str])
def get_algorithms() -> list[str]:
    return get_algorithm_names()


@router.post(
    "/generate-grid",
    response_model=GenerateGridResponse,
)
def generate_grid(
    request: GenerateGridRequest,
) -> GenerateGridResponse:

    start = Node(
        request.start.row,
        request.start.col,
    )

    goal = Node(
        request.goal.row,
        request.goal.col,
    )

    grid = create_random_grid(
        rows=request.rows,
        cols=request.cols,
        start=start,
        goal=goal,
        obstacle_probability=request.obstacle_probability,
        seed=request.seed,
    )

    return GenerateGridResponse(
        grid=grid_to_schema(grid),
    )


@router.post(
    "/search",
    response_model=BenchmarkResponse,
)
def search(
    request: SearchRequest,
) -> BenchmarkResponse:

    algorithm = get_algorithm(
        request.algorithm,
    )

    recorder = SearchEventRecorder()

    runtime_ms, memory_bytes, result = benchmark_search(
        algorithm,
        grid_from_schema(request.grid),
        node_from_schema(request.start),
        node_from_schema(request.goal),
        recorder,
    )

    payload = BenchmarkResponse(
        algorithm=request.algorithm,
        runtime_ms=runtime_ms,
        memory_bytes=memory_bytes,
        result=search_result_to_schema(result),
    )

    return payload


@router.post("/search/compare", response_model=ComparisonResponse)
def compare_search(request: ComparisonRequest) -> ComparisonResponse:
    results = compare_algorithms(
        grid_from_schema(request.grid),
        node_from_schema(request.start),
        node_from_schema(request.goal),
    )

    comparison_results = [
        AlgorithmComparisonResult(
            algorithm=algorithm,
            runtime_ms=runtime_ms,
            memory_bytes=memory_bytes,
            path_found=result.path_found,
            path_length=result.path_length,
            nodes_expanded=result.nodes_expanded,
            nodes_discovered=result.nodes_discovered,
            total_cost=result.total_cost,
        )
        for algorithm, (runtime_ms, memory_bytes, result) in results.items()
    ]

    return ComparisonResponse(results=comparison_results)
