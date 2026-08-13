"use client";

import { useState, useEffect, useCallback } from "react";
import { createDefaultEditorState } from "@/lib/grid/createDefaultEditorState";
import { GridDensity } from "@/types/editor";
import { api } from "@/lib/api";
import { DENSITY_PROBABILITY } from "@/lib/grid/density";
import { updateCell } from "@/lib/grid/updateCell";
import { BenchmarkResults } from "@/types/metrics";
import { ComparisonResponse } from "@/types/comparison";

const ANIMATION_DELAY_MS = 16;
const DEFAULT_SIZE = 25;

export function useGridSearch() {
  const [editor, setEditor] = useState(() => createDefaultEditorState());
  const [size, setSize] = useState(DEFAULT_SIZE);
  const [density, setDensity] = useState<GridDensity>("empty");
  const [benchmarkResult, setBenchmarkResult] =
    useState<BenchmarkResults | null>(null);
  const [comparison, setComparison] = useState<ComparisonResponse | null>(null);

  const [isSearching, setIsSearching] = useState(false);
  const [isComparing, setIsComparing] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // ─── Derived / helpers ───────────────────────────────────────────

  const clearResults = useCallback(() => {
    setEditor((prev) => ({
      ...prev,
      path: [],
      events: [],
      animationIndex: 0,
      searchResult: null,
    }));
    setBenchmarkResult(null);
    setError(null);
  }, []);

  // ─── Core actions ────────────────────────────────────────────────

  const runSearch = useCallback(async () => {
    if (isSearching || isComparing) return;

    setIsSearching(true);
    setError(null);
    setBenchmarkResult(null);

    try {
      const response = await api.search({
        grid: editor.grid,
        start: editor.start,
        goal: editor.goal,
        algorithm: editor.algorithm,
      });

      setBenchmarkResult({
        runtime: response.runtime_ms,
        memory: response.memory_bytes,
      });

      const result = response.result;

      setEditor((prev) => ({
        ...prev,
        path: result.path,
        events: result.events,
        animationIndex: 0,
        searchResult: result,
      }));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Search failed");
      clearResults();
    } finally {
      setIsSearching(false);
    }
  }, [
    editor.grid,
    editor.start,
    editor.goal,
    editor.algorithm,
    isSearching,
    clearResults,
  ]);

  const runComparison = useCallback(async () => {
    if (isSearching || isComparing) return;

    setIsComparing(true);
    setError(null);

    try {
      const response = await api.compareAlgorithms({
        grid: editor.grid,
        start: editor.start,
        goal: editor.goal,
      });
      setComparison(response);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Algorithm comparison failed",
      );
    } finally {
      setIsComparing(false);
    }
  }, [editor.grid, editor.start, editor.goal, isSearching, isComparing]);

  const generateGrid = useCallback(async () => {
    if (isGenerating) return;

    setIsGenerating(true);
    setError(null);
    setComparison(null);

    const sizeChanged = editor.grid.cells.length !== size;

    const start = sizeChanged ? { row: 0, col: 0 } : editor.start;

    const goal = sizeChanged ? { row: size - 2, col: size - 2 } : editor.goal;

    try {
      const response = await api.generateGrid({
        rows: size,
        cols: size,
        obstacle_probability: DENSITY_PROBABILITY[density],
        start: start,
        goal: goal,
      });

      setEditor((prev) => ({
        ...prev,
        grid: response.grid,
        start,
        goal,
        path: [],
        events: [],
        animationIndex: 0,
        searchResult: null,
      }));
      setBenchmarkResult(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Grid generation failed");
    } finally {
      setIsGenerating(false);
    }
  }, [size, density, editor.start, editor.goal, isGenerating]);

  // ─── Editor mutation handlers ────────────────────────────────────

  const handleAlgorithmChange = useCallback((algorithm: string) => {
    setEditor((prev) => ({
      ...prev,
      algorithm,
    }));
  }, []);

  const handleCellChange = useCallback(
    (row: number, col: number, blocked: boolean) => {
      setEditor((prev) => ({
        ...prev,
        grid: updateCell(prev.grid, row, col, blocked),
        // clear results on edit
        path: [],
        events: [],
        animationIndex: 0,
        searchResult: null,
      }));
      setBenchmarkResult(null);
    },
    [],
  );

  const handleMoveStart = useCallback((row: number, col: number) => {
    setEditor((prev) => ({
      ...prev,
      start: { row, col },
      path: [],
      events: [],
      animationIndex: 0,
      searchResult: null,
    }));
    setBenchmarkResult(null);
  }, []);

  const handleMoveGoal = useCallback((row: number, col: number) => {
    setEditor((prev) => ({
      ...prev,
      goal: { row, col },
      path: [],
      events: [],
      animationIndex: 0,
      searchResult: null,
    }));
    setBenchmarkResult(null);
  }, []);

  // ─── Animation ───────────────────────────────────────────────────

  useEffect(() => {
    if (
      editor.animationIndex >= editor.events.length ||
      editor.events.length === 0
    ) {
      return;
    }

    const timer = setTimeout(() => {
      setEditor((prev) => ({
        ...prev,
        animationIndex: prev.animationIndex + 8,
      }));
    }, ANIMATION_DELAY_MS);

    return () => clearTimeout(timer);
  }, [editor.animationIndex, editor.events.length]);

  // ─── Keyboard shortcuts ──────────────────────────────────────────

  useEffect(() => {
    const toolMap: Record<string, "start" | "goal" | "wall"> = {
      s: "start",
      g: "goal",
      w: "wall",
    };

    function handleKeyDown(event: KeyboardEvent) {
      // Don't steal keys while typing in inputs
      if (
        event.target instanceof HTMLInputElement ||
        event.target instanceof HTMLTextAreaElement ||
        event.target instanceof HTMLSelectElement
      ) {
        return;
      }

      const tool = toolMap[event.key.toLowerCase()];
      if (tool) {
        event.preventDefault();
        setEditor((prev) => ({ ...prev, tool }));
      }
    }

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  // ─── Public API ──────────────────────────────────────────────────

  return {
    // State
    editor,
    size,
    density,
    benchmarkResult,
    isSearching,
    isComparing,
    isGenerating,
    error,
    comparison,

    // Setters for controls
    setSize,
    setDensity,

    // Actions
    runSearch,
    generateGrid,
    clearResults,
    runComparison,

    // Handlers for GridView / selectors
    handleAlgorithmChange,
    handleCellChange,
    handleMoveStart,
    handleMoveGoal,
  };
}
