from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.models.grid import Grid
from grid_search.models.node import Node


def reconstruct_path(
    parents: dict[Node, Node],
    current: Node,
    recorder: SearchEventRecorder | None = None,
) -> list[Node]:
    path = [current]

    while current in parents:
        current = parents[current]
        path.append(current)

    path.reverse()

    if recorder:
        for node in path:
            recorder.record_path(node)

    return path


def calculate_path_cost(
    grid: Grid,
    path: list[Node],
) -> int:
    if len(path) < 2:
        return 0

    return sum(grid.get_cost(node) for node in path[1:])
