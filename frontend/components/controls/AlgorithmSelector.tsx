import { useEffect, useState } from "react";
import { api } from "@/lib/api";
import Select from "../ui/Select";
import { ALGORITHM_INFO } from "@/lib/algorithms/algorithmInfo";

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

  const options = algorithms.map((algorithm) => ({
    value: algorithm,
    label: ALGORITHM_INFO[algorithm]?.name ?? algorithm,
  }));

  return (
    <Select value={algorithm} options={options} onChange={onAlgorithmChange} />
  );
}
