export interface GridNode {
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
  start: GridNode;
  goal: GridNode;
  obstacle_probability: number;
  seed?: number;
}

export interface SearchRequest {
  algorithm: string;
  grid: Grid;
  start: GridNode;
  goal: GridNode;
}

export interface SearchResult {
  path: GridNode[];
  visited: GridNode[];
  path_found: boolean;
  path_length: number | null;
  nodes_expanded: number;
  nodes_discovered: number;
  total_cost: number | null;
}
