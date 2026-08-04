from dataclasses import dataclass


@dataclass
class BenchmarkRecord:
    scenario: str
    algorithm: str
    grid_size: int
    obstacle_probability: float
    run: int

    runtime_ms: float
    memory_bytes: int

    path_found: bool
    path_length: int | None

    nodes_expanded: int
    nodes_discovered: int

    total_cost: int | None
