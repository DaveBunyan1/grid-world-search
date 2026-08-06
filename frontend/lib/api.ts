import { API_BASE_URL } from "./config";
import {
  GenerateGridRequest,
  Grid,
  SearchRequest,
  SearchResult,
} from "@/types/api";

async function request<T>(endpoint: string, options?: RequestInit): Promise<T> {
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

export function getAlgorithms() {
  return request<string[]>("/algorithms");
}

export function generateGrid(body: GenerateGridRequest) {
  return request<{ grid: Grid }>("/generate-grid", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

export function search(body: SearchRequest) {
  return request<SearchResult>("/search", {
    method: "POST",
    body: JSON.stringify(body),
  });
}
