from typing import Protocol

from grid_search.models.node import Node


class Graph(Protocol):
    def get_neighbours(self, node: Node) -> list[Node]: ...

    def get_edge_cost(
        self,
        source: Node,
        destination: Node,
    ) -> int: ...
