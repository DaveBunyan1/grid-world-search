from grid_search.models.node import Node


def manhattan_distance(
    current: Node,
    goal: Node,
) -> int:
    return abs(current.row - goal.row) + abs(current.col - goal.col)
