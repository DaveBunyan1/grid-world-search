interface MetricProps {
  label: string;
  value: string | number;
}

export default function Metric({ label, value }: MetricProps) {
  return (
    <div className="flex items-center justify-between gap-4 py-2">
      <span className="text-sm text-slate-400">{label}</span>

      <span className="text-sm font-semibold text-slate-100 text-right">
        {value}
      </span>
    </div>
  );
}
