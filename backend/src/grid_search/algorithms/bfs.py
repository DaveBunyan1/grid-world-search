from collections import deque

from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.algorithms.search_state import SearchState
from grid_search.algorithms.utils import reconstruct_path
from grid_search.models.grid import Grid
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def bfs(
    grid: Grid, start: Node, goal: Node, recorder: SearchEventRecorder | None = None
) -> SearchResult:

    frontier = deque([start])

    state = SearchState(start, recorder)

    while frontier:
        current = frontier.popleft()

        state.expand(current)

        if current == goal:
            return SearchResult(
                path=reconstruct_path(state.parents, current, recorder),
                expanded_nodes=state.expanded_nodes,
                nodes_expanded=state.nodes_expanded,
                nodes_discovered=state.nodes_discovered,
                events=state.events,
            )

        for neighbour in grid.get_neighbours(current):
            if state.discover(current, neighbour):
                frontier.append(neighbour)

    return SearchResult(
        path=None,
        expanded_nodes=state.expanded_nodes,
        nodes_expanded=state.nodes_expanded,
        nodes_discovered=state.nodes_discovered,
        events=state.events,
    )
