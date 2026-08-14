from grid_search.api.schemas import (
    CellSchema,
    GridSchema,
    NodeSchema,
    SearchEventSchema,
    SearchResponse,
)
from grid_search.graphs.grid import Grid
from grid_search.models.cell import Cell
from grid_search.models.node import Node
from grid_search.models.search_event import SearchEvent
from grid_search.models.search_result import SearchResult


def grid_to_schema(grid: Grid) -> GridSchema:
    return GridSchema(
        cells=[
            [
                CellSchema(
                    blocked=cell.blocked,
                    cost=cell.cost,
                )
                for cell in row
            ]
            for row in grid.cells
        ]
    )


def node_from_schema(node: NodeSchema) -> Node:
    return Node(
        row=node.row,
        col=node.col,
    )


def grid_from_schema(grid: GridSchema) -> Grid:
    return Grid(
        cells=[
            [
                Cell(
                    blocked=cell.blocked,
                    cost=cell.cost,
                )
                for cell in row
            ]
            for row in grid.cells
        ]
    )


def search_event_to_schema(
    event: SearchEvent,
) -> SearchEventSchema:

    return SearchEventSchema(
        event_type=event.event_type,
        node=NodeSchema(
            row=event.node.row,
            col=event.node.col,
        ),
        g_cost=event.g_cost,
        h_cost=event.h_cost,
    )


def search_result_to_schema(
    result: SearchResult,
) -> SearchResponse:
    path = (
        []
        if result.path is None
        else [
            NodeSchema(
                row=node.row,
                col=node.col,
            )
            for node in result.path
        ]
    )

    return SearchResponse(
        path=path,
        events=[search_event_to_schema(event) for event in result.events],
        expanded_nodes=[
            NodeSchema(
                row=node.row,
                col=node.col,
            )
            for node in result.expanded_nodes
        ],
        path_found=result.path_found,
        path_length=result.path_length,
        nodes_expanded=result.nodes_expanded,
        nodes_discovered=result.nodes_discovered,
        total_cost=result.total_cost,
    )
