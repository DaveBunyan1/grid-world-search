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
    visited: list[NodeSchema]

    path_found: bool

    path_length: int | None

    nodes_expanded: int

    nodes_discovered: int

    total_cost: int | None


class GenerateGridResponse(BaseModel):
    grid: GridSchema
