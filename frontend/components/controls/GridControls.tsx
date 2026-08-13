"use client";

import { GridDensity } from "@/types/editor";
import Button from "../ui/Button";
import Select from "../ui/Select";

const sizeOptions = [
  { value: "25", label: "25 × 25" },
  { value: "50", label: "50 × 50" },
];

const densityOptions = [
  { value: "empty", label: "Empty" },
  { value: "sparse", label: "Sparse" },
  { value: "dense", label: "Dense" },
];

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
    <div className="flex gap-4">
      <Select
        value={String(size)}
        options={sizeOptions}
        onChange={(value) => onSizeChange(Number(value))}
      />

      <Select
        value={density}
        options={densityOptions}
        onChange={(value) => onDensityChange(value as GridDensity)}
      />

      <Button onClick={onGenerate}>Generate Grid</Button>
    </div>
  );
}
