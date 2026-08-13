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

  onGenerateUnweighted(): void;
  onGenerateWeighted(): void;
}

export default function GridControls({
  size,
  density,
  onSizeChange,
  onDensityChange,
  onGenerateUnweighted,
  onGenerateWeighted,
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

      <Button onClick={onGenerateUnweighted}>Generate Grid</Button>
      <Button onClick={onGenerateWeighted}>Generate Weighted Grid</Button>
    </div>
  );
}
