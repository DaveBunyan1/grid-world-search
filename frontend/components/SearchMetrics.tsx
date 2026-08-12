import type { SearchResult } from "@/types/api";

interface SearchMetricsProps {
  result: SearchResult;
}

export default function SearchMetrics({ result }: SearchMetricsProps) {
  return (
    <div className="grid grid-cols-2 gap-3">
      <Metric label="Nodes Expanded" value={result.nodes_expanded} />

      <Metric label="Nodes Discovered" value={result.nodes_discovered} />

      <Metric label="Path Length" value={result.path_length ?? "—"} />

      <Metric label="Path Cost" value={result.total_cost ?? "—"} />

      <Metric label="Path Found" value={result.path_found ? "Yes" : "No"} />
    </div>
  );
}

interface MetricProps {
  label: string;
  value: string | number;
}

function Metric({ label, value }: MetricProps) {
  return (
    <div className="rounded-md border border-slate-700 bg-slate-800/50 p-3">
      <div className="text-xs text-slate-400">{label}</div>

      <div className="mt-1 text-lg font-semibold text-slate-100">{value}</div>
    </div>
  );
}
