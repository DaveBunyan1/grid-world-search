import { Grid, GridNode } from "./api";

export interface AlgorithmComparisonResult {
  algorithm: string;
  runtime_ms: number;
  memory_bytes: number;

  path_found: boolean;
  path_length: number | null;

  nodes_expanded: number;
  nodes_discovered: number;

  total_cost: number | null;
}

export interface ComparisonResponse {
  results: AlgorithmComparisonResult[];
}

export interface ComparisonRequest {
  grid: Grid;
  start: GridNode;
  goal: GridNode;
}
