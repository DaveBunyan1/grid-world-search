import { Grid } from "@/types/api";

export function updateCellCost(
  grid: Grid,
  row: number,
  col: number,
  cost: number,
): Grid {
  return {
    cells: grid.cells.map((cellsRow, r) =>
      cellsRow.map((cell, c) =>
        r === row && c === col ? { ...cell, cost } : cell,
      ),
    ),
  };
}
