import { AlgorithmComparisonResult } from "@/types/comparison";
import {
  ComparisonRow,
  formatAlgorithmName,
  formatMemory,
} from "./ComparisonHelpers";
import { useMemo } from "react";

interface AlgorithmComparisonProps {
  results: AlgorithmComparisonResult[];
}

function formatRepresentationName(name: string): string {
  // "adjacency_list" → "Adjacency list", "grid" → "Grid"
  return name
    .split("_")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

export default function AlgorithmComparison({
  results,
}: AlgorithmComparisonProps) {
  const representations = useMemo(() => {
    const seen = new Set<string>();
    const ordered: string[] = [];

    for (const result of results) {
      for (const rep of result.representations) {
        if (!seen.has(rep.representation)) {
          seen.add(rep.representation);
          ordered.push(rep.representation);
        }
      }
    }

    return ordered;
  }, [results]);

  if (results.length === 0) {
    return null;
  }

  function getRepMetrics(result: AlgorithmComparisonResult, repName: string) {
    return result.representations.find((r) => r.representation === repName);
  }

  return (
    <section className="mt-6">
      <h2 className="mb-4 text-lg font-semibold text-slate-100">
        Algorithm Comparison
      </h2>

      <div className="overflow-x-auto rounded-md border border-slate-700">
        <table className="w-full border-collapse text-sm">
          <thead>
            <tr className="bg-slate-800/70">
              <th className="px-4 py-3 text-left font-medium text-slate-400">
                Metric
              </th>

              {results.map((result) => (
                <th
                  key={result.algorithm}
                  className="px-4 py-3 text-left font-semibold text-slate-100"
                >
                  {formatAlgorithmName(result.algorithm)}
                </th>
              ))}
            </tr>
          </thead>

          <tbody>
            <ComparisonRow
              label="Nodes Expanded"
              values={results.map((result) => result.nodes_expanded)}
            />

            <ComparisonRow
              label="Nodes Discovered"
              values={results.map((result) => result.nodes_discovered)}
            />

            <ComparisonRow
              label="Path Length"
              values={results.map((result) => result.path_length ?? "—")}
            />

            <ComparisonRow
              label="Path Cost"
              values={results.map((result) => result.total_cost ?? "—")}
            />

            <ComparisonRow
              label="Path Found"
              values={results.map((result) =>
                result.path_found ? "Yes" : "No",
              )}
            />

            {representations.map((repName) => (
              <>
                <ComparisonRow
                  key={`${repName}-runtime`}
                  label={`${formatRepresentationName(repName)} — Runtime`}
                  values={results.map((result) => {
                    const metrics = getRepMetrics(result, repName);
                    return metrics
                      ? `${metrics.runtime_ms.toFixed(2)} ms`
                      : "—";
                  })}
                />
                <ComparisonRow
                  key={`${repName}-memory`}
                  label={`${formatRepresentationName(repName)} — Memory`}
                  values={results.map((result) => {
                    const metrics = getRepMetrics(result, repName);
                    return metrics ? formatMemory(metrics.memory_bytes) : "—";
                  })}
                />
              </>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
