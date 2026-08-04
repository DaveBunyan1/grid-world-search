import heapq
from itertools import count

from grid_search.algorithms.heuristics import manhattan_distance
from grid_search.algorithms.utils import reconstruct_path
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def astar(
    grid: Grid,
    start: Node,
    goal: Node,
) -> SearchResult:

    counter = count()

    frontier: list[tuple[int, int, Node]] = [(0, next(counter), start)]

    discovered = {start}

    parents: dict[Node, Node] = {}

    cost_so_far = {start: 0}

    nodes_expanded = 0

    while frontier:
        _, _, current = heapq.heappop(frontier)

        nodes_expanded += 1

        if current == goal:
            return SearchResult(
                path=reconstruct_path(parents, current),
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

                priority = new_cost + manhattan_distance(neighbour, goal)

                heapq.heappush(
                    frontier,
                    (
                        priority,
                        next(counter),
                        neighbour,
                    ),
                )

    return SearchResult(
        path=None,
        nodes_expanded=nodes_expanded,
        nodes_discovered=len(discovered),
        total_cost=None,
    )
