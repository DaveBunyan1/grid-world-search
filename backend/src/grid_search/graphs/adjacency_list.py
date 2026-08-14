from grid_search.graphs.graph import Graph
from grid_search.models.cell import Cell
from grid_search.models.node import Node


class AdjacencyListGraph(Graph):
    """
    Graph stored as:
        node -> list of (neighbour, edge_cost)
    """

    def __init__(self, adjacency: dict[Node, list[tuple[Node, int]]]):
        self._adjacency = adjacency

    @classmethod
    def from_cells(cls, cells: list[list[Cell]]) -> AdjacencyListGraph:
        """Build an adjacency list from a 2D grid of cells."""
        rows = len(cells)
        cols = len(cells[0]) if rows else 0
        adjacency: dict[Node, list[tuple[Node, int]]] = {}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if cells[r][c].blocked:
                    continue

                node = Node(r, c)
                neighbours: list[tuple[Node, int]] = []

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not cells[nr][nc].blocked:
                        dest = Node(nr, nc)
                        # Same cost rule as Grid: cost of entering destination
                        cost = cells[nr][nc].cost
                        neighbours.append((dest, cost))

                adjacency[node] = neighbours

        return cls(adjacency)

    def get_neighbours(self, node: Node) -> list[Node]:
        return [neighbour for neighbour, _ in self._adjacency.get(node, [])]

    def get_edge_cost(self, source: Node, destination: Node) -> int:
        for neighbour, cost in self._adjacency.get(source, []):
            if neighbour == destination:
                return cost
        raise ValueError(f"No edge from {source} to {destination}")
