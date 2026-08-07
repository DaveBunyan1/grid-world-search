"use client";

import { GridDensity } from "@/types/editor";

interface GridControlsProps {
  size: number;
  density: GridDensity;

  onSizeChange(size: number): void;

  onDensityChange(density: GridDensity): void;

  onGenerate(): void;
}

export default function GridControls({
  size,
  density,
  onSizeChange,
  onDensityChange,
  onGenerate,
}: GridControlsProps) {
  return (
    <div className="flex gap-4 mb-4">
      <select
        value={size}
        onChange={(e) => onSizeChange(Number(e.target.value))}
      >
        <option value={25}>25 x 25</option>

        <option value={50}>50 x 50</option>

        <option value={100}>100 x 100</option>
      </select>

      <select
        value={density}
        onChange={(e) => onDensityChange(e.target.value as GridDensity)}
      >
        <option value="empty">Empty</option>

        <option value="sparse">Sparse</option>

        <option value="dense">Dense</option>
      </select>

      <button onClick={onGenerate} className="border px-4 py-2">
        Generate Grid
      </button>
    </div>
  );
}
