export interface Node {
  row: number;
  col: number;
}

export interface Cell {
  blocked: boolean;
  cost: number;
}

export interface Grid {
  cells: Cell[][];
}

export interface GenerateGridRequest {
  rows: number;
  cols: number;
  obstacle_probability: number;
  seed?: number;
}

export interface SearchRequest {
  algorithm: string;
  grid: Grid;
  start: Node;
  goal: Node;
}

export interface SearchResult {
  path: Node[];
  path_found: boolean;
  path_length: number | null;
  nodes_expanded: number;
  nodes_discovered: number;
  total_cost: number | null;
}
