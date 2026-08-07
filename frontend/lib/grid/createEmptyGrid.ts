import { Cell, Grid } from "@/types/api";

export function createEmptyGrid(rows: number, cols: number): Grid {
  const cells: Cell[][] = [];

  for (let row = 0; row < rows; row++) {
    const currentRow: Cell[] = [];

    for (let col = 0; col < cols; col++) {
      currentRow.push({
        blocked: false,
        cost: 1,
      });
    }

    cells.push(currentRow);
  }

  return {
    cells,
  };
}
