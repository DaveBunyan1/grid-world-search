from grid_search.algorithms.search_event_recorder import SearchEventRecorder
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
