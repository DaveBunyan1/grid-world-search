interface ComparisonRowProps {
  label: string;
  values: (string | number)[];
}

export function ComparisonRow({ label, values }: ComparisonRowProps) {
  return (
    <tr className="border-t border-slate-800">
      <td className="whitespace-nowrap px-4 py-3 text-slate-400">{label}</td>

      {values.map((value, index) => (
        <td
          key={index}
          className="whitespace-nowrap px-4 py-3 font-medium text-slate-100"
        >
          {value}
        </td>
      ))}
    </tr>
  );
}

export function formatMemory(bytes: number): string {
  if (bytes < 1024) {
    return `${bytes} B`;
  }

  if (bytes < 1024 * 1024) {
    return `${(bytes / 1024).toFixed(1)} KB`;
  }

  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

export function formatAlgorithmName(algorithm: string): string {
  const names: Record<string, string> = {
    bfs: "BFS",
    dfs: "DFS",
    dijkstra: "Dijkstra",
    astar: "A*",
  };

  return names[algorithm.toLowerCase()] ?? algorithm;
}
