from abc import ABC, abstractmethod

from grid_search.models.node import Node


class Graph(ABC):
    @abstractmethod
    def get_neighbours(self, node: Node) -> list[Node]: ...

    @abstractmethod
    def get_edge_cost(
        self,
        source: Node,
        destination: Node,
    ) -> int: ...
