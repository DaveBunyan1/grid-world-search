import heapq
from itertools import count

from grid_search.algorithms.heuristics import manhattan_distance
from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.algorithms.search_state import SearchState
from grid_search.algorithms.utils import reconstruct_path
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def astar(
    grid: Grid,
    start: Node,
    goal: Node,
    recorder: SearchEventRecorder | None = None,
) -> SearchResult:

    counter = count()

    frontier: list[tuple[int, int, Node]] = [(0, next(counter), start)]

    state = SearchState(start, recorder)

    cost_so_far = {start: 0}

    while frontier:
        _, _, current = heapq.heappop(frontier)

        state.expand(current)

        if current == goal:
            return SearchResult(
                path=reconstruct_path(state.parents, current, recorder),
                expanded_nodes=state.expanded_nodes,
                nodes_expanded=state.nodes_expanded,
                nodes_discovered=state.nodes_discovered,
                total_cost=cost_so_far[current],
                events=state.events,
            )

        for neighbour in grid.get_neighbours(current):
            new_cost = cost_so_far[current] + grid.get_cost(neighbour)

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost

                state.update_parent(current, neighbour)

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
        expanded_nodes=state.expanded_nodes,
        nodes_expanded=state.nodes_expanded,
        nodes_discovered=state.nodes_discovered,
        total_cost=None,
        events=state.events,
    )
