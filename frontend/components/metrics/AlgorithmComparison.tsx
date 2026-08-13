import { AlgorithmComparisonResult } from "@/types/comparison";
import {
  ComparisonRow,
  formatAlgorithmName,
  formatMemory,
} from "./ComparisonHelpers";

interface AlgorithmComparisonProps {
  results: AlgorithmComparisonResult[];
}

export default function AlgorithmComparison({
  results,
}: AlgorithmComparisonProps) {
  if (results.length === 0) {
    return null;
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

            <ComparisonRow
              label="Runtime"
              values={results.map(
                (result) => `${result.runtime_ms.toFixed(2)} ms`,
              )}
            />

            <ComparisonRow
              label="Memory"
              values={results.map((result) =>
                formatMemory(result.memory_bytes),
              )}
            />
          </tbody>
        </table>
      </div>
    </section>
  );
}
