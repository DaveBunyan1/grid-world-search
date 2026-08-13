import { ALGORITHM_INFO } from "@/lib/algorithms/algorithmInfo";
import Metric from "@/components/metrics/Metric";

interface AlgorithmInfoProps {
  algorithm: string;
}

export default function AlgorithmInfo({ algorithm }: AlgorithmInfoProps) {
  const info = ALGORITHM_INFO[algorithm];

  if (!info) {
    return null;
  }
  return (
    <div className="grid grid-cols-1 gap-0.5">
      <h2>{info.name}</h2>

      <Metric label="Time complexity:" value={info.timeComplexity} />
      <Metric label="Space" value={info.spaceComplexity} />
      <Metric label="Frontier" value={info.frontier} />
      <Metric label="Optimal" value={info.optimal} />

      {info.heuristic && <Metric label="Heuristic" value={info.heuristic} />}
    </div>
  );
}
