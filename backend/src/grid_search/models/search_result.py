from dataclasses import dataclass

from grid_search.models.node import Node
from grid_search.models.search_event import SearchEvent


@dataclass
class SearchResult:
    path: list[Node] | None
    expanded_nodes: list[Node]
    nodes_expanded: int
    nodes_discovered: int
    events: list[SearchEvent]
    total_cost: int | None = None

    @property
    def path_found(self) -> bool:
        return self.path is not None

    @property
    def path_length(self) -> int | None:
        if self.path is None:
            return None

        return len(self.path)
