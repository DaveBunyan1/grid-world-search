"use client";

import { useState, useEffect } from "react";

import GridView from "@/components/grid/GridView";
import GridControls from "@/components/controls/GridControls";

import { createDefaultEditorState } from "@/lib/grid/createDefaultEditorState";
import { GridDensity } from "@/types/editor";

import { api } from "@/lib/api";
import { DENSITY_PROBABILITY } from "@/lib/grid/density";
import { updateCell } from "@/lib/grid/updateCell";
import AlgorithmSelector from "@/components/controls/AlgorithmSelector";
import SearchMetrics from "@/components/SearchMetrics";
import BenchmarkMetrics from "@/components/BenchmarkMetrics";

export default function Home() {
  const [editor, setEditor] = useState(() => createDefaultEditorState());

  const [size, setSize] = useState(25);

  const [density, setDensity] = useState<GridDensity>("empty");

  const [runtimeMs, setRuntimeMs] = useState(0);
  const [memoryBytes, setMemoryBytes] = useState(0);

  function handleAlgorithmChange(algorithm: string) {
    setEditor((previous) => ({
      ...previous,
      algorithm,
    }));
  }

  async function runSearch() {
    const response = await api.search({
      grid: editor.grid,
      start: editor.start,
      goal: editor.goal,
      algorithm: editor.algorithm,
    });

    setRuntimeMs(response.runtime_ms);
    setMemoryBytes(response.memory_bytes);

    const result = response.result;

    console.log(result);
    setEditor((previous) => ({
      ...previous,
      path: result.path,
      events: result.events,
      animationIndex: 0,
      searchResult: result,
    }));
  }

  useEffect(() => {
    if (editor.animationIndex >= editor.events.length) {
      return;
    }

    const timer = setTimeout(() => {
      setEditor((previous) => ({
        ...previous,
        animationIndex: previous.animationIndex + 1,
      }));
    }, 1);

    return () => clearTimeout(timer);
  }, [editor.animationIndex, editor.events.length]);

  useEffect(() => {
    function handleKeyDown(event: KeyboardEvent) {
      if (event.key === "s") {
        setEditor((previous) => ({
          ...previous,
          tool: "start",
        }));
      }

      if (event.key === "g") {
        setEditor((previous) => ({
          ...previous,
          tool: "goal",
        }));
      }

      if (event.key === "w") {
        setEditor((previous) => ({
          ...previous,
          tool: "wall",
        }));
      }
    }

    window.addEventListener("keydown", handleKeyDown);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  function handleMoveStart(row: number, col: number) {
    setEditor((previous) => ({
      ...previous,
      start: {
        row,
        col,
      },
    }));
  }

  function handleMoveGoal(row: number, col: number) {
    setEditor((previous) => ({
      ...previous,
      goal: {
        row,
        col,
      },
    }));
  }

  function handleCellChange(row: number, col: number, blocked: boolean) {
    setEditor((previous) => ({
      ...previous,
      grid: updateCell(previous.grid, row, col, blocked),
    }));
  }

  async function generateGrid() {
    const start = editor.start;

    const goal = editor.goal;

    const response = await api.generateGrid({
      rows: size,
      cols: size,
      obstacle_probability: DENSITY_PROBABILITY[density],
      start,
      goal,
    });

    setEditor((previous) => ({
      ...previous,
      grid: response.grid,
      start,
      goal,
      path: [],
      events: [],
      searchResult: null,
    }));
  }

  return (
    <main className="p-8">
      <GridControls
        size={size}
        density={density}
        onSizeChange={setSize}
        onDensityChange={setDensity}
        onGenerate={generateGrid}
      />

      <AlgorithmSelector
        algorithm={editor.algorithm}
        onAlgorithmChange={handleAlgorithmChange}
      />

      <button onClick={runSearch} className="px-4 py-2 border rounded">
        Search
      </button>
      <div className="flex">
        <GridView
          editor={editor}
          onCellChange={handleCellChange}
          onMoveStart={handleMoveStart}
          onMoveGoal={handleMoveGoal}
        />
        {editor.searchResult && <SearchMetrics result={editor.searchResult} />}
        {editor.searchResult && (
          <BenchmarkMetrics runtime_ms={runtimeMs} memory_bytes={memoryBytes} />
        )}
      </div>
    </main>
  );
}
