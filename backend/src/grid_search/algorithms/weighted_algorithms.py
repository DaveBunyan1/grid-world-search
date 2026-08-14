import heapq
import itertools
import math
from collections.abc import Callable

from grid_search.algorithms.heuristics import manhattan_distance
from grid_search.algorithms.search_event_recorder import SearchEventRecorder
from grid_search.algorithms.search_state import SearchState
from grid_search.algorithms.utils import reconstruct_path
from grid_search.graphs.graph import Graph
from grid_search.models.node import Node
from grid_search.models.search_result import SearchResult


def _best_first(
    graph: Graph,
    start: Node,
    goal: Node,
    priority: Callable[[Node, float], float],
    recorder: SearchEventRecorder | None = None,
) -> SearchResult:
    counter = itertools.count()

    frontier: list[tuple[float, int, Node]] = [
        (priority(start, 0), next(counter), start)
    ]

    state = SearchState(start, recorder)

    cost_so_far = {start: 0}

    in_heap: set[Node] = {start}
    closed: set[Node] = set()

    while frontier:
        _, _, current = heapq.heappop(frontier)
        in_heap.discard(current)

        if current in closed:
            continue
        closed.add(current)

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

        base_score = cost_so_far[current]

        for neighbour in graph.get_neighbours(current):
            if neighbour in closed:
                continue

            tentative_score = base_score + graph.get_edge_cost(current, neighbour)

            if tentative_score < cost_so_far.get(neighbour, math.inf):
                if neighbour not in cost_so_far:
                    state.discover(current, neighbour)
                elif tentative_score < cost_so_far[neighbour]:
                    state.update_parent(current, neighbour)

                cost_so_far[neighbour] = tentative_score

                heapq.heappush(
                    frontier,
                    (priority(neighbour, tentative_score), next(counter), neighbour),
                )
                in_heap.add(neighbour)

    return SearchResult(
        path=None,
        expanded_nodes=state.expanded_nodes,
        nodes_expanded=state.nodes_expanded,
        nodes_discovered=state.nodes_discovered,
        total_cost=None,
        events=state.events,
    )


def dijkstra(
    graph: Graph, start: Node, goal: Node, recorder: SearchEventRecorder | None = None
) -> SearchResult:
    return _best_first(graph, start, goal, priority=lambda _, g: g, recorder=recorder)


def astar(
    graph: Graph,
    start: Node,
    goal: Node,
    recorder: SearchEventRecorder | None = None,
    heuristic: Callable[[Node, Node], int] = manhattan_distance,
) -> SearchResult:
    return _best_first(
        graph,
        start,
        goal,
        priority=lambda node, g: g + heuristic(node, goal),
        recorder=recorder,
    )
