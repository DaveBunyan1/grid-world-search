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
    GenerateGridRequest,
    GenerateGridResponse,
    SearchRequest,
    SearchResponse,
)
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
    response_model=SearchResponse,
)
def search(
    request: SearchRequest,
) -> SearchResponse:

    algorithm = get_algorithm(
        request.algorithm,
    )

    recorder = SearchEventRecorder()

    result = algorithm(
        grid_from_schema(request.grid),
        node_from_schema(request.start),
        node_from_schema(request.goal),
        recorder,
    )

    return search_result_to_schema(result)
