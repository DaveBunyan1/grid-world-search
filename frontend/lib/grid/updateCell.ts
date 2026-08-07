import { Grid } from "@/types/api";

export function updateCell(
  grid: Grid,
  row: number,
  col: number,
  blocked: boolean,
): Grid {
  return {
    ...grid,
    cells: grid.cells.map((currentRow, rowIndex) =>
      currentRow.map((cell, colIndex) => {
        if (rowIndex === row && colIndex === col) {
          return {
            ...cell,
            blocked,
          };
        }

        return cell;
      }),
    ),
  };
}
