from grid_search.models.node import Node
from grid_search.models.search_event import (
    EventType,
    SearchEvent,
)


class SearchEventRecorder:
    def __init__(self):
        self.events: list[SearchEvent] = []

    def record_frontier_add(
        self,
        node: Node,
        g_cost: float | None = None,
        h_cost: float | None = None,
    ) -> None:
        self.events.append(
            SearchEvent(
                event_type=EventType.FRONTIER_ADD,
                node=node,
                g_cost=g_cost,
                h_cost=h_cost,
            )
        )

    def record_expand(
        self,
        node: Node,
        g_cost: float | None = None,
        h_cost: float | None = None,
    ) -> None:
        self.events.append(
            SearchEvent(
                event_type=EventType.EXPAND,
                node=node,
                g_cost=g_cost,
                h_cost=h_cost,
            )
        )

    def record_path(
        self,
        node: Node,
    ) -> None:
        self.events.append(
            SearchEvent(
                event_type=EventType.PATH,
                node=node,
            )
        )

    def get_events(self) -> list[SearchEvent]:
        return self.events.copy()
