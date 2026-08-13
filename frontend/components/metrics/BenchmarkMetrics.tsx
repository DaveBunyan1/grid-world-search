import { BenchmarkResults } from "@/types/metrics";
import Metric from "./Metric";

interface BenchmarkMetricsProps {
  benchmarkResults: BenchmarkResults;
}

export default function BenchmarkMetrics({
  benchmarkResults,
}: BenchmarkMetricsProps) {
  return (
    <div className="grid grid-cols-1 gap-0.5">
      <h2>Benchmark metrics</h2>

      <Metric
        label="Runtime (ms)"
        value={`${benchmarkResults.runtime.toFixed(2)} ms`}
      />

      <Metric
        label="Memory (bytes)"
        value={`${(benchmarkResults.memory / 1024).toFixed(1)} KB`}
      />
    </div>
  );
}
