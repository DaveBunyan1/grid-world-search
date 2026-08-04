from grid_search.models.node import Node


class Grid:
    def __init__(self, cells: list[list[str]]):
        self.cells = cells

    def get_neighbours(self, node: Node) -> list[Node]:
        positions = [
            (node.row - 1, node.col),
            (node.row + 1, node.col),
            (node.row, node.col - 1),
            (node.row, node.col + 1),
        ]

        return [
            Node(row, col) for row, col in positions if self.is_valid_position(row, col)
        ]

    def is_valid_position(self, row: int, col: int) -> bool:
        return (
            0 <= row < len(self.cells)
            and 0 <= col < len(self.cells[0])
            and self.cells[row][col] != "#"
        )
