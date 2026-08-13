import { SearchResult } from "@/types/api";

import AlgorithmInfo from "./AlgorithmInfo";
import LiveRunStats from "./LiveRunStats";
import { BenchmarkResults } from "@/types/metrics";
import BenchmarkMetrics from "./BenchmarkMetrics";

type MetricSidebarProps = {
  algorithm: string;
  searchResult: SearchResult;
  benchmark: BenchmarkResults;
};

const MetricSidebar = ({
  algorithm,
  searchResult,
  benchmark,
}: MetricSidebarProps) => {
  return (
    <aside className="flex flex-col gap-6">
      <AlgorithmInfo algorithm={algorithm} />

      <LiveRunStats result={searchResult} />

      <BenchmarkMetrics benchmarkResults={benchmark} />
    </aside>
  );
};

export default MetricSidebar;
