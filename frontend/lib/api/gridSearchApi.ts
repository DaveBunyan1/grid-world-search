import {
  GenerateGridRequest,
  Grid,
  SearchRequest,
  SearchResult,
} from "@/types/api";

export interface GridSearchApi {
  getAlgorithms(): Promise<string[]>;

  generateGrid(request: GenerateGridRequest): Promise<{ grid: Grid }>;

  search(request: SearchRequest): Promise<SearchResult>;
}
