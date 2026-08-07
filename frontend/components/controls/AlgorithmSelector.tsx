import { useEffect, useState } from "react";
import { api } from "@/lib/api";

interface AlgorithmSelectorProps {
  algorithm: string;

  onAlgorithmChange(algorithm: string): void;
}

export default function AlgorithmSelector({
  algorithm,
  onAlgorithmChange,
}: AlgorithmSelectorProps) {
  const [algorithms, setAlgorithms] = useState<string[]>([]);

  useEffect(() => {
    async function loadAlgorithms() {
      const result = await api.getAlgorithms();

      setAlgorithms(result);
    }

    loadAlgorithms();
  }, []);

  return (
    <select
      value={algorithm}
      onChange={(event) => onAlgorithmChange(event.target.value)}
    >
      {algorithms.map((algorithm) => (
        <option key={algorithm} value={algorithm}>
          {algorithm}
        </option>
      ))}
    </select>
  );
}
