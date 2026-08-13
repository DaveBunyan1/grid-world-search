"use client";

import GridView from "@/components/grid/GridView";
import GridControls from "@/components/controls/GridControls";
import AlgorithmSelector from "@/components/controls/AlgorithmSelector";
import MetricSidebar from "@/components/metrics/MetricSidebar";
import { useGridSearch } from "@/hooks/useGridSearch";
import Button from "@/components/ui/Button";
import AlgorithmComparison from "@/components/metrics/AlgorithmComparison";

export default function Home() {
  const {
    editor,
    size,
    density,
    benchmarkResult,
    isSearching,
    isComparing,
    isGenerating,
    error,
    comparison,
    gridType,
    setSize,
    setDensity,
    runSearch,
    runComparison,
    generateGrid,
    handleAlgorithmChange,
    handleCellChange,
    handleMoveStart,
    handleMoveGoal,
  } = useGridSearch();

  const isBusy = isSearching || isGenerating;

  return (
    <main className="min-h-screen pt-4 px-6 bg-gray-950">
      <header className="mb-4">
        <h1 className="text-2xl font-semibold tracking-tight text-slate-50">
          Grid World Search
        </h1>
        <p className="mt-1 text-sm text-slate-400">
          Visualize pathfinding algorithms on a customizable grid.
        </p>
      </header>
      <div className="flex flex-col gap-6 ">
        <aside className="flex w-full gap-4 lg:w-auto shrink-0">
          <GridControls
            size={size}
            density={density}
            onSizeChange={setSize}
            onDensityChange={setDensity}
            onGenerateUnweighted={() => generateGrid("unweighted")}
            onGenerateWeighted={() => generateGrid("weighted")}
          />

          <AlgorithmSelector
            algorithm={editor.algorithm}
            onAlgorithmChange={handleAlgorithmChange}
          />

          <Button onClick={runSearch} disabled={isBusy}>
            {isSearching ? "Searching…" : "Run Search"}
          </Button>

          <Button onClick={runComparison} disabled={isBusy}>
            {isComparing ? "Comparing..." : "Compare"}
          </Button>

          {error && (
            <p className="rounded-md bg-red-50 px-3 py-2 text-sm text-red-700">
              {error}
            </p>
          )}
        </aside>
        <div className="flex gap-5">
          <GridView
            editor={editor}
            gridType={gridType}
            onCellChange={handleCellChange}
            onMoveStart={handleMoveStart}
            onMoveGoal={handleMoveGoal}
          />
          {editor.searchResult && benchmarkResult && (
            <MetricSidebar
              algorithm={editor.algorithm}
              searchResult={editor.searchResult}
              benchmark={benchmarkResult}
            />
          )}
          {comparison && <AlgorithmComparison results={comparison.results} />}
        </div>
      </div>
    </main>
  );
}
