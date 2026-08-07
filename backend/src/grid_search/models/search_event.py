from dataclasses import dataclass
from enum import StrEnum

from grid_search.models.node import Node


class EventType(StrEnum):
    FRONTIER_ADD = "frontier_add"  # Node queued/discovered
    EXPAND = "expand"  # Node popped & expanded
    PATH = "path"  # Final reconstructed path node


@dataclass(frozen=True)
class SearchEvent:
    event_type: EventType
    node: Node
    g_cost: float | None = None
    h_cost: float | None = None
