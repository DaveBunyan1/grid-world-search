# Grid World Search

An interactive pathfinding visualizer and benchmarking application for comparing graph search algorithms on grid-based environments.

The project combines algorithm visualization, performance benchmarking, weighted graphs, and algorithm comparison in a full-stack application.

---

## Features

- Interactive grid editor
- Random grid generation
- Adjustable grid size and obstacle density
- Start and goal node placement
- Animated search visualization
- Custom cell weights
- Weighted and unweighted grids
- Algorithm performance comparison
- Runtime and memory benchmarking
- Search metrics including:
  - Nodes expanded
  - Nodes discovered
  - Path length
  - Path cost
  - Path found

### Search Algorithms

Currently implemented:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra's Algorithm
- A\* Search

### Algorithm comparison

The application can run all algorithms against the same grid and compare
their:

- Runtime
- Memory usage
- Nodes expanded
- Nodes discovered
- Path length
- Path cost

On weighted graphs, this also demonstrates the difference between minimizing
the number of edges and minimizing total path cost.

### Grid Generation

- Random weighted and unweighted grid generation
- Configurable obstacle density
- Reproducible grids using random seeds

### Benchmarking

The benchmarking suite measures:

- Runtime
- Peak memory usage
- Nodes expanded
- Nodes discovered
- Path length
- Success rate

Benchmarks can be executed across multiple:

- Grid sizes
- Obstacle densities
- Random seeds

Results are exported as CSV files and can be analysed using pandas or visualised using Seaborn.

---

## Architecture

The project consists of a Next.js frontend and a Python/FastAPI backend.

```text
┌──────────────────────┐
│      Next.js         │
│      Frontend        │
│                      │
│  Grid visualization  │
│  Controls & metrics  │
└──────────┬───────────┘
           │ HTTP
           ▼
┌──────────────────────┐
│       FastAPI        │
│       Backend        │
│                      │
│ Search algorithms    │
│ Grid generation      │
│ Benchmarking         │
└──────────────────────┘
```

### Backend

- Python
- FastAPI
- pytest
- dataclasses
- tracemalloc
- perf_counter

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

---

## Running Locally

### Prerequisites

- Docker Desktop

### Docker Compose

The easiest way to run the application is with Docker Compose.

Clone the repository:

```bash
git clone <repository-url>
cd grid-world-search
```

Start the application:

```bash
docker compose up --build
```

The frontend will be available at:

```text
http://localhost:3000
```

The backend API will be available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

To stop the application:

```bash
docker compose down
```

## Running Without Docker

### Backend

```bash
cd backend

pip install -e ".[dev]"

python -m pytest
```

Start the API:

```bash
uvicorn grid_search.api.app:app --reload
```

### Frontend

```bash
cd frontend

npm install
npm run dev
```

The frontend will be available at:

```text
http://localhost:3000
```

## Docker

Both the frontend and backend are containerized.

Build the containers:

```bash
docker compose build
```

Run them:

```bash
docker compose up
```

The Docker setup is also used by CI to verify that both applications can be built successfully.

## Project Structure

```text
grid-world-search/
├── backend/
│   ├── src/
│   │   └── grid_search/
│   │       ├── algorithms/
│   │       ├── api/
│   │       ├── benchmarks/
│   │       ├── generators/
│   │       └── models/
│   ├── tests/
│   ├── Dockerfile
│   └── pyproject.toml
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── types/
│   ├── Dockerfile
│   └── package.json
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
└── README.md
```

---

## Running Benchmarks

Execute the benchmark suite:

```bash
python src/scripts/run_benchmarks.py
```

Analyse benchmark results:

```bash
python src/scripts/analyse_benchmark.py
```

Generate benchmark plots:

```bash
python src/scripts/plot_benchmarks.py
```

Generated figures are written to:

```text
docs/benchmark_results/
```

---

## Documentation

Additional documentation can be found in the `docs/` directory.

Current documentation includes:

- Benchmark methodology
- Benchmark results
- Performance analysis

---

## Current Status

### Completed

- Grid representation
- Random grid generation
- BFS
- DFS
- Dijkstra
- A\*
- Benchmarking framework
- CSV export
- Benchmark analysis
- Benchmark visualisation
- FastAPI backend
- Interactive frontend
- Search visualisation and animation
- Algorithm Comparison
- Weighted Grids
- Custom cell weights
- Docker
- GitHub Actions CI
- Alternative graph representations
- Comparison of alternative graph representations

### In Progress

- Additional search algorithms
- Maze generation
- Performance optimisations

---

## License

This project is intended as a learning project for exploring graph search algorithms, software architecture, benchmarking, and interactive algorithm visualisation.
