from grid_search.graphs.graph import Graph
from grid_search.models.cell import Cell
from grid_search.models.node import Node


class AdjacencyMatrix(Graph):
    """
    Dense N x N cost matrix.
    0 => no edge (grid costs are assumed >= 1).
    """

    def __init__(
        self,
        matrix: list[list[int]],
        index_to_node: list[Node],
        node_to_index: dict[Node, int],
    ):
        self._matrix = matrix
        self._index_to_node = index_to_node
        self._node_to_index = node_to_index
        self._n = len(index_to_node)

    @classmethod
    def from_cells(cls, cells: list[list[Cell]]) -> AdjacencyMatrix:
        rows = len(cells)
        cols = len(cells[0]) if rows else 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        index_to_node: list[Node] = []
        node_to_index: dict[Node, int] = {}

        for r in range(rows):
            for c in range(cols):
                if not cells[r][c].blocked:
                    node = Node(r, c)
                    node_to_index[node] = len(index_to_node)
                    index_to_node.append(node)

        n = len(index_to_node)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for node in index_to_node:
            i = node_to_index[node]
            for dr, dc in directions:
                nr, nc = node.row + dr, node.col + dc
                if 0 <= nr < rows and 0 <= nc < cols and not cells[nr][nc].blocked:
                    dest = Node(nr, nc)
                    j = node_to_index[dest]
                    matrix[i][j] = cells[nr][nc].cost

        return cls(matrix, index_to_node, node_to_index)

    def get_neighbours(self, node: Node) -> list[Node]:
        i = self._node_to_index[node]
        row = self._matrix[i]
        return [self._index_to_node[j] for j in range(self._n) if row[j] != 0]

    def get_edge_cost(self, source: Node, destination: Node) -> int:
        i = self._node_to_index[source]
        j = self._node_to_index[destination]
        cost = self._matrix[i][j]
        if cost == 0:
            raise ValueError(f"No edge from {source} to {destination}")
        return cost
