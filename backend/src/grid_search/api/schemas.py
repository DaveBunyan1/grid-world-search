from typing import Literal

from pydantic import BaseModel


class NodeSchema(BaseModel):
    row: int
    col: int


class CellSchema(BaseModel):
    blocked: bool
    cost: int


class GridSchema(BaseModel):
    cells: list[list[CellSchema]]


class SearchEventSchema(BaseModel):
    event_type: str
    node: NodeSchema
    g_cost: float | None = None
    h_cost: float | None = None


class GenerateGridRequest(BaseModel):
    rows: int
    cols: int
    obstacle_probability: float = 0.2
    start: NodeSchema
    goal: NodeSchema
    seed: int | None = None


class SearchRequest(BaseModel):
    algorithm: Literal[
        "bfs",
        "dfs",
        "dijkstra",
        "astar",
    ]

    grid: GridSchema

    start: NodeSchema
    goal: NodeSchema


class SearchResponse(BaseModel):
    path: list[NodeSchema]
    events: list[SearchEventSchema]

    expanded_nodes: list[NodeSchema]
    path_found: bool

    path_length: int | None

    nodes_expanded: int

    nodes_discovered: int

    total_cost: int | None


class BenchmarkResponse(BaseModel):
    algorithm: str
    runtime_ms: float
    memory_bytes: int
    result: SearchResponse


class GenerateGridResponse(BaseModel):
    grid: GridSchema


class AlgorithmComparisonResult(BaseModel):
    algorithm: str
    runtime_ms: float
    memory_bytes: int

    path_found: bool
    path_length: int | None

    nodes_expanded: int
    nodes_discovered: int

    total_cost: int | None


class ComparisonRequest(BaseModel):
    grid: GridSchema

    start: NodeSchema
    goal: NodeSchema


class ComparisonResponse(BaseModel):
    results: list[AlgorithmComparisonResult]
