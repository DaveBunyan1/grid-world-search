import type { SearchResult } from "@/types/api";
import Metric from "./Metric";

interface SearchMetricsProps {
  result: SearchResult;
}

export default function LiveRunStats({ result }: SearchMetricsProps) {
  return (
    <div className="grid grid-cols-1 gap-0.5">
      <h2>Live Run Stats</h2>
      <Metric label="Nodes Expanded" value={result.nodes_expanded} />

      <Metric label="Nodes Discovered" value={result.nodes_discovered} />

      <Metric label="Path Length" value={result.path_length ?? "—"} />

      <Metric label="Path Cost" value={result.total_cost ?? "—"} />

      <Metric label="Path Found" value={result.path_found ? "Yes" : "No"} />
    </div>
  );
}
