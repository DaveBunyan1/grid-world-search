"use client";

import { EditorState } from "@/types/editor";
import CellView from "./CellView";
import { useState } from "react";

interface GridViewProps {
  editor: EditorState;

  onCellChange(row: number, col: number, blocked: boolean): void;

  onMoveStart(row: number, col: number): void;

  onMoveGoal(row: number, col: number): void;
}

export default function GridView({
  editor,
  onCellChange,
  onMoveStart,
  onMoveGoal,
}: GridViewProps) {
  const [mouseDown, setMouseDown] = useState(false);

  const [dragMode, setDragMode] = useState<boolean | null>(null);

  function handleMouseDown(row: number, col: number, button: number) {
    if (editor.tool === "start") {
      onMoveStart(row, col);
      return;
    }

    if (editor.tool === "goal") {
      onMoveGoal(row, col);
      return;
    }

    const blocked = button === 0;

    setMouseDown(true);
    setDragMode(blocked);

    onCellChange(row, col, blocked);
  }

  function handleMouseEnter(row: number, col: number) {
    if (mouseDown && dragMode !== null) {
      onCellChange(row, col, dragMode);
    }
  }

  return (
    <div
      className="grid"
      onMouseUp={() => {
        setMouseDown(false);
        setDragMode(null);
      }}
      onMouseLeave={() => {
        setMouseDown(false);
        setDragMode(null);
      }}
      style={{
        gridTemplateColumns: `repeat(${editor.grid.cells[0].length}, 1.5rem)`,
      }}
    >
      {editor.grid.cells.map((row, rowIndex) =>
        row.map((cell, colIndex) => {
          const isPath = editor.path.some(
            (node) => node.row === rowIndex && node.col === colIndex,
          );
          const isVisited = editor.visited.some(
            (node) => node.row === rowIndex && node.col === colIndex,
          );

          return (
            <CellView
              key={`${rowIndex}-${colIndex}`}
              cell={cell}
              position={{
                row: rowIndex,
                col: colIndex,
              }}
              isStart={
                editor.start.row === rowIndex && editor.start.col === colIndex
              }
              isGoal={
                editor.goal.row === rowIndex && editor.goal.col === colIndex
              }
              isPath={isPath}
              isVisited={isVisited}
              onMouseDown={handleMouseDown}
              onMouseEnter={handleMouseEnter}
            />
          );
        }),
      )}
    </div>
  );
}
