from dataclasses import dataclass


@dataclass(frozen=True)
class Cell:
    cost: int = 1
    blocked: bool = False
