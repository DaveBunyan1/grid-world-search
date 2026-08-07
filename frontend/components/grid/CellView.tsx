import { Cell } from "@/types/api";

interface CellViewProps {
  cell: Cell;

  position: {
    row: number;
    col: number;
  };

  isStart: boolean;

  isGoal: boolean;

  isPath: boolean;
  isVisited: boolean;

  onMouseDown(row: number, col: number, button: number): void;

  onMouseEnter(row: number, col: number): void;
}

export default function CellView({
  cell,
  position,
  isStart,
  isGoal,
  isPath,
  isVisited,
  onMouseDown,
  onMouseEnter,
}: CellViewProps) {
  let className = "w-6 h-6 border";

  if (isStart) {
    className += " bg-green-500";
  } else if (isGoal) {
    className += " bg-red-500";
  } else if (cell.blocked) {
    className += " bg-black";
  } else if (isPath) {
    className += " bg-yellow-400";
  } else if (isVisited) {
    className += " bg-purple-400";
  } else {
    className += " bg-sky-900";
  }

  return (
    <div
      onMouseDown={(event) => {
        event.preventDefault();

        if (isStart || isGoal) {
          return;
        }

        onMouseDown(position.row, position.col, event.button);
      }}
      onMouseEnter={() => {
        if (!isStart && !isGoal) {
          onMouseEnter(position.row, position.col);
        }
      }}
      onContextMenu={(event) => event.preventDefault()}
      className={className}
    />
  );
}
