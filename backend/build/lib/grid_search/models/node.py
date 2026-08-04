from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    row: int
    col: int
