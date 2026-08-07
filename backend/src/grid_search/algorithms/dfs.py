from grid_search.algorithms.utils import reconstruct_path
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def dfs(grid: Grid, start: Node, goal: Node) -> SearchResult:
    frontier = [start]

    discovered = {start}
    visited = []

    parents: dict[Node, Node] = {}

    nodes_expanded = 0

    while frontier:
        current = frontier.pop()
        visited.append(current)

        nodes_expanded += 1

        if current == goal:
            return SearchResult(
                path=reconstruct_path(parents, current),
                visited=visited,
                nodes_expanded=nodes_expanded,
                nodes_discovered=len(discovered),
            )

        for neighbour in grid.get_neighbours(current):
            if neighbour not in discovered:
                discovered.add(neighbour)

                parents[neighbour] = current

                frontier.append(neighbour)

    return SearchResult(
        path=None,
        visited=[],
        nodes_expanded=nodes_expanded,
        nodes_discovered=len(discovered),
    )
