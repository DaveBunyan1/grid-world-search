import {
  BenchmarkResult,
  GenerateGridRequest,
  Grid,
  SearchRequest,
  SearchResult,
} from "@/types/api";
import { API_BASE_URL } from "../config";
import { GridSearchApi } from "./gridSearchApi";

class HttpGridSearchApi implements GridSearchApi {
  private async request<T>(
    endpoint: string,
    options?: RequestInit,
  ): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        "Content-Type": "application/json",
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    return response.json() as Promise<T>;
  }

  async getAlgorithms() {
    return this.request<string[]>("/algorithms");
  }

  async generateGrid(request: GenerateGridRequest): Promise<{ grid: Grid }> {
    return this.request("/generate-grid", {
      method: "POST",
      body: JSON.stringify(request),
    });
  }

  async search(request: SearchRequest): Promise<BenchmarkResult> {
    return this.request("/search", {
      method: "POST",
      body: JSON.stringify(request),
    });
  }
}

export const api = new HttpGridSearchApi();
