from dataclasses import dataclass

from grid_search.models.node import Node


@dataclass
class SearchResult:
    path: list[Node] | None
    nodes_expanded: int
    nodes_discovered: int
