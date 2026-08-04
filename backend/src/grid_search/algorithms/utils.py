from grid_search.models.node import Node


def reconstruct_path(parents: dict[Node, Node], current: Node) -> list[Node]:
    path = [current]

    while current in parents:
        current = parents[current]
        path.append(current)

    path.reverse()

    return path
