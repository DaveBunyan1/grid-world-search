import {
  BenchmarkResult,
  GenerateGridRequest,
  Grid,
  SearchRequest,
} from "@/types/api";
import { ComparisonRequest, ComparisonResponse } from "@/types/comparison";

export interface GridSearchApi {
  getAlgorithms(): Promise<string[]>;

  generateGrid(request: GenerateGridRequest): Promise<{ grid: Grid }>;

  search(request: SearchRequest): Promise<BenchmarkResult>;

  compareAlgorithms(request: ComparisonRequest): Promise<ComparisonResponse>;
}
