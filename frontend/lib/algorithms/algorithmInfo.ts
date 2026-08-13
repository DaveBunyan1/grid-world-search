interface AlgorithmInfo {
  name: string;
  timeComplexity: string;
  spaceComplexity: string;
  frontier: string;
  optimal: string;
  heuristic?: string;
}

export const ALGORITHM_INFO: Record<string, AlgorithmInfo> = {
  bfs: {
    name: "Breadth-First Search",
    timeComplexity: "O(V + E)",
    spaceComplexity: "O(V)",
    frontier: "FIFO queue",
    optimal: "Yes — unweighted graph",
  },

  dfs: {
    name: "Depth-First Search",
    timeComplexity: "O(V + E)",
    spaceComplexity: "O(V)",
    frontier: "LIFO stack",
    optimal: "No",
  },

  dijkstra: {
    name: "Dijkstra's",
    timeComplexity: "O((V + E) log V)",
    spaceComplexity: "O(V)",
    frontier: "Min-priority queue (binary heap)",
    optimal: "Yes — non-negative edge weights",
  },

  astar: {
    name: "A*",
    timeComplexity: "O((V + E) log V)",
    spaceComplexity: "O(V)",
    frontier: "Min-priority queue (binary heap)",
    optimal: "Yes — with admissible heuristic",
    heuristic: "Manhattan distance",
  },
};
