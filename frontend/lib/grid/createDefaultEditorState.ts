import { DEFAULT_GRID_SIZE } from "../config";
import { createEmptyGrid } from "./createEmptyGrid";

import { EditorState } from "@/types/editor";

export function createDefaultEditorState(): EditorState {
  const rows = DEFAULT_GRID_SIZE;
  const cols = DEFAULT_GRID_SIZE;

  return {
    grid: createEmptyGrid(rows, cols),

    start: {
      row: 1,
      col: 1,
    },

    goal: {
      row: rows - 2,
      col: cols - 2,
    },

    tool: "wall",

    algorithm: "astar",
    path: [],
    events: [],

    animationIndex: 0,
    searchResult: null,
  };
}
