from dataclasses import dataclass


@dataclass
class BenchmarkConfig:
    scenario: str
    size: int
    obstacle_probability: float
    runs: int = 5


sizes = [100, 250, 500, 1000]

scenarios = [
    ("open", 0.0),
    ("sparse", 0.1),
    ("dense", 0.3),
]


BENCHMARKS = [
    BenchmarkConfig(
        scenario=scenario,
        size=size,
        obstacle_probability=obstacle_probability,
    )
    for size in sizes
    for scenario, obstacle_probability in scenarios
]
