from grid_search.graphs.graph import Graph
from grid_search.models.cell import Cell
from grid_search.models.node import Node


class CSR(Graph):
    """
    offsets[i] .. offsets[i+1] index into neighbours/weights
    for the node with dense index i.
    """

    def __init__(
        self,
        offsets: list[int],
        neighbours: list[int],
        weights: list[int],
        index_to_node: list[Node],
        node_to_index: dict[Node, int],
    ):
        self._offsets = offsets
        self._neighbours = neighbours
        self._weights = weights
        self._index_to_node = index_to_node
        self._node_to_index = node_to_index

    @classmethod
    def from_cells(cls, cells: list[list[Cell]]) -> CSR:
        rows = len(cells)
        cols = len(cells[0]) if rows else 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Only traversable cells become nodes
        index_to_node: list[Node] = []
        node_to_index: dict[Node, int] = {}

        for r in range(rows):
            for c in range(cols):
                if not cells[r][c].blocked:
                    node = Node(r, c)
                    node_to_index[node] = len(index_to_node)
                    index_to_node.append(node)

        offsets: list[int] = [0]
        neighbours: list[int] = []
        weights: list[int] = []

        for node in index_to_node:
            for dr, dc in directions:
                nr, nc = node.row + dr, node.col + dc
                if 0 <= nr < rows and 0 <= nc < cols and not cells[nr][nc].blocked:
                    dest = Node(nr, nc)
                    neighbours.append(node_to_index[dest])
                    weights.append(cells[nr][nc].cost)
            offsets.append(len(neighbours))

        return cls(offsets, neighbours, weights, index_to_node, node_to_index)

    def get_neighbours(self, node: Node) -> list[Node]:
        i = self._node_to_index[node]
        start, end = self._offsets[i], self._offsets[i + 1]
        return [self._index_to_node[j] for j in self._neighbours[start:end]]

    def get_edge_cost(self, source: Node, destination: Node) -> int:
        i = self._node_to_index[source]
        dest_i = self._node_to_index[destination]
        start, end = self._offsets[i], self._offsets[i + 1]

        for k in range(start, end):
            if self._neighbours[k] == dest_i:
                return self._weights[k]

        raise ValueError(f"No edge from {source} to {destination}")
