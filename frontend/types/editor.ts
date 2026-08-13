import { Grid, GridNode, SearchEvent, SearchResult } from "./api";

export interface EditorState {
  grid: Grid;
  start: GridNode;
  goal: GridNode;
  tool: EditorTool;
  algorithm: string;

  path: GridNode[];
  events: SearchEvent[];

  animationIndex: number;
  searchResult: SearchResult | null;
}

export type GridDensity = "empty" | "sparse" | "dense";

export interface GridGenerationConfig {
  size: number;
  density: GridDensity;
}

export type EditorTool = "wall" | "start" | "goal";
