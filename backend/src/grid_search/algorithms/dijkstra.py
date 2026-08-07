import heapq
from itertools import count

from grid_search.algorithms.utils import reconstruct_path
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def dijkstra(
    grid: Grid,
    start: Node,
    goal: Node,
) -> SearchResult:

    counter = count()

    frontier: list[tuple[int, int, Node]] = [(0, next(counter), start)]

    discovered = {start}
    visited = []

    parents: dict[Node, Node] = {}

    cost_so_far = {start: 0}

    nodes_expanded = 0

    while frontier:
        current_cost, _, current = heapq.heappop(frontier)
        visited.append(current)

        if current_cost > cost_so_far[current]:
            continue

        nodes_expanded += 1

        if current == goal:
            return SearchResult(
                path=reconstruct_path(parents, current),
                visited=visited,
                nodes_expanded=nodes_expanded,
                nodes_discovered=len(discovered),
                total_cost=cost_so_far[current],
            )

        for neighbour in grid.get_neighbours(current):
            new_cost = cost_so_far[current] + grid.get_cost(neighbour)

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                parents[neighbour] = current
                discovered.add(neighbour)

                heapq.heappush(
                    frontier,
                    (new_cost, next(counter), neighbour),
                )

    return SearchResult(
        path=None,
        visited=[],
        nodes_expanded=nodes_expanded,
        nodes_discovered=len(discovered),
        total_cost=None,
    )
