from grid_search.algorithms.search_event_recorder import (
    SearchEventRecorder,
)
from grid_search.models.node import Node
from grid_search.models.search_event import SearchEvent


class SearchState:
    def __init__(
        self,
        start: Node,
        recorder: SearchEventRecorder | None = None,
    ):
        self.discovered: set[Node] = {start}
        self.expanded_nodes: list[Node] = []
        self.parents: dict[Node, Node] = {}

        self.recorder = recorder

        if self.recorder:
            self.recorder.record_frontier_add(start)

    def discover(
        self,
        parent: Node,
        child: Node,
    ) -> bool:
        """
        Records a newly discovered node.

        Returns True if the node was newly discovered,
        False if it had already been seen.
        """

        if child in self.discovered:
            return False

        self.discovered.add(child)
        self.parents[child] = parent

        if self.recorder:
            self.recorder.record_frontier_add(child)

        return True

    def update_parent(
        self,
        parent: Node,
        child: Node,
    ) -> None:
        self.parents[child] = parent

    def expand(self, node: Node) -> None:
        self.expanded_nodes.append(node)

        if self.recorder:
            self.recorder.record_expand(node)

    @property
    def nodes_expanded(self) -> int:
        return len(self.expanded_nodes)

    @property
    def nodes_discovered(self) -> int:
        return len(self.discovered)

    @property
    def events(self) -> list[SearchEvent]:
        if self.recorder is None:
            return []

        return self.recorder.get_events()
