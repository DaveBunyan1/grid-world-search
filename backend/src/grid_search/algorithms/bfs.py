from collections import deque

from grid_search.grid import Grid
from grid_search.models.node import Node


def bfs(grid: Grid, start: Node, goal: Node):
    frontier = deque([start])

    visited = {start}

    parents = {}

    while frontier:
        current = frontier.popleft()

        if current == goal:
            return reconstruct_path(parents, current)

        for neighbour in grid.get_neighbours(current):
            if neighbour not in visited:
                visited.add(neighbour)

                parents[neighbour] = current

                frontier.append(neighbour)

    return None


def reconstruct_path(parents: dict[Node, Node], current: Node) -> list[Node]:
    path = [current]

    while current in parents:
        current = parents[current]
        path.append(current)

    path.reverse()

    return path
