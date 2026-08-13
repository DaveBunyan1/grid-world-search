import { Cell } from "@/types/api";
import { useMemo } from "react";

export type CellVisualState =
  | "start"
  | "goal"
  | "blocked"
  | "path"
  | "visited"
  | "frontier"
  | "empty";

interface CellViewProps {
  cell: Cell;
  position: {
    row: number;
    col: number;
  };
  isStart: boolean;
  isGoal: boolean;
  isPath: boolean;
  isExpanded: boolean;
  isFrontier: boolean;
  showWeight: boolean;
  costRange?: { min: number; max: number };
  onMouseDown(row: number, col: number, button: number): void;
  onMouseEnter(row: number, col: number): void;
}

function costToHeatmapColor(t: number): string {
  // Clamp
  const v = Math.max(0, Math.min(1, t));

  // You can swap this for any palette you like
  const r = Math.round(30 + (100 - 30) * v);
  const g = Math.round(41 + (116 - 41) * v);
  const b = Math.round(59 + (139 - 59) * v);

  return `rgb(${r}, ${g}, ${b})`;
}

export default function CellView({
  cell,
  position,
  isStart,
  isGoal,
  isPath,
  isExpanded,
  isFrontier,
  showWeight,
  costRange = { min: 1, max: 10 },
  onMouseDown,
  onMouseEnter,
}: CellViewProps) {
  // Determine active visual state using priority order
  const visualState: CellVisualState = useMemo(() => {
    if (isStart) return "start";
    if (isGoal) return "goal";
    if (cell.blocked) return "blocked";
    if (isPath) return "path";
    if (isExpanded) return "visited";
    if (isFrontier) return "frontier";
    return "empty";
  }, [isStart, isGoal, cell.blocked, isPath, isExpanded, isFrontier]);

  // Color & styling map
  const stateStyles: Record<CellVisualState, string> = {
    start:
      "bg-emerald-500 shadow-lg shadow-emerald-500/50 scale-95 rounded-sm z-10",
    goal: "bg-rose-500 shadow-lg shadow-rose-500/50 scale-95 rounded-sm z-10",
    blocked: "bg-black border-slate-300/50",
    path: "bg-amber-400 shadow-md shadow-amber-400/40 animate-path-pop z-10 border-gray-700",
    visited: "bg-indigo-600/80 animate-visited-pop border-slate-100/30",
    frontier: "bg-teal-400/70 animate-frontier-pop border-teal-300/40",
    empty:
      "bg-slate-800 border-slate-600/60 hover:bg-slate-800/50 transition-colors",
  };

  const heatmapStyle =
    visualState === "empty"
      ? {
          backgroundColor: costToHeatmapColor(
            (cell.cost - costRange.min) / (costRange.max - costRange.min || 1),
          ),
        }
      : undefined;

  const isInteractive = !isStart && !isGoal;

  return (
    <div
      onMouseDown={(event) => {
        event.preventDefault();
        if (isInteractive) {
          onMouseDown(position.row, position.col, event.button);
        }
      }}
      onMouseEnter={() => {
        if (isInteractive) {
          onMouseEnter(position.row, position.col);
        }
      }}
      onContextMenu={(event) => event.preventDefault()}
      style={heatmapStyle}
      className={`
        w-6 h-6 border-[0.5px] select-none transition-all duration-150 ease-out flex items-center justify-center
        ${visualState !== "empty" ? stateStyles[visualState] : "border-slate-600/40 hover:brightness-110"}
        ${isInteractive ? "cursor-pointer" : "cursor-default"}
      `}
    >
      {isStart && <span className="text-white text-[10px] font-black">S</span>}
      {isGoal && <span className="text-white text-[10px] font-black">G</span>}

      {showWeight && !isStart && !isGoal && !cell.blocked && (
        <span className="text-[9px] font-semibold text-slate-200">
          {cell.cost}
        </span>
      )}
    </div>
  );
}
