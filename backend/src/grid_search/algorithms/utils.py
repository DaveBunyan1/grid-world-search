from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.models.graph import Graph
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
    graph: Graph,
    path: list[Node],
) -> int:
    if len(path) < 2:
        return 0

    return sum(
        graph.get_edge_cost(source, destination)
        for source, destination in zip(path, path[1:], strict=False)
    )
