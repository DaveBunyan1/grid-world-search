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
  events: SearchEvent[];
  expanded_nodes: GridNode[];
  path_found: boolean;
  path_length: number | null;
  nodes_expanded: number;
  nodes_discovered: number;
  total_cost: number | null;
}

export type SearchEventType = "frontier_add" | "expand" | "path";

export interface SearchEvent {
  event_type: SearchEventType;

  node: GridNode;

  g_cost: number | null;

  h_cost: number | null;
}

export interface BenchmarkResult {
  algorithm: string;
  runtime_ms: number;
  memory_bytes: number;
  result: SearchResult;
}
