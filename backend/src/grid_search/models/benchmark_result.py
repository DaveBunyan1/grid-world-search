from dataclasses import dataclass

from grid_search.models.search_result import SearchResult


@dataclass
class BenchmarkResult:
    algorithm: str
    runtime_ms: float
    memory_bytes: int
    search_result: SearchResult
