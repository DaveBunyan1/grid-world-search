from grid_search.graphs.graph import Graph
from grid_search.models.cell import Cell
from grid_search.models.node import Node


class AdjacencyListWithCostMap(Graph):
    """
    node -> list[neighbour]
    (source, destination) -> edge cost
    """

    def __init__(
        self,
        adjacency: dict[Node, list[Node]],
        edge_costs: dict[tuple[Node, Node], int],
    ):
        self._adjacency = adjacency
        self._edge_costs = edge_costs

    @classmethod
    def from_cells(cls, cells: list[list[Cell]]) -> AdjacencyListWithCostMap:
        rows = len(cells)
        cols = len(cells[0]) if rows else 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        adjacency: dict[Node, list[Node]] = {}
        edge_costs: dict[tuple[Node, Node], int] = {}

        for r in range(rows):
            for c in range(cols):
                if cells[r][c].blocked:
                    continue

                node = Node(r, c)
                neighbours: list[Node] = []

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not cells[nr][nc].blocked:
                        dest = Node(nr, nc)
                        neighbours.append(dest)
                        edge_costs[(node, dest)] = cells[nr][nc].cost

                adjacency[node] = neighbours

        return cls(adjacency, edge_costs)

    def get_neighbours(self, node: Node) -> list[Node]:
        return self._adjacency.get(node, [])

    def get_edge_cost(self, source: Node, destination: Node) -> int:
        try:
            return self._edge_costs[(source, destination)]
        except KeyError as exc:
            raise ValueError(f"No edge from {source} to {destination}") from exc
