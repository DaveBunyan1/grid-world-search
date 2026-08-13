export type AlgorithmInformation = {
  // To be replaced with endpoint
  algorithm_name: string;
  time_complexity: string;
  space: string;
  frontier: string;
  optimal: string;
};

export type BenchmarkResults = {
  runtime: number;
  memory: number;
};
