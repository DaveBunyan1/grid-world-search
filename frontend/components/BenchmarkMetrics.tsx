interface BenchmarkMetricsProps {
  runtime_ms: number;
  memory_bytes: number;
}

export default function SearchMetrics({
  runtime_ms,
  memory_bytes,
}: BenchmarkMetricsProps) {
  return (
    <div className="grid grid-cols-2 gap-3">
      <Metric label="Runtime (ms)" value={runtime_ms} />

      <Metric label="Memory (bytes)" value={memory_bytes} />
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
