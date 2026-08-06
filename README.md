# Grid World Search

A Python project for implementing, comparing, and visualising classical graph search algorithms on grid-based environments.

The project explores both the theoretical and practical behaviour of search algorithms through benchmarking, documentation, and an interactive frontend (currently in development).

---

## Features

### Search Algorithms

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra's Algorithm
- A\* Search

### Grid Generation

- Random grid generation
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

## Project Structure

```text
backend/
├── docs/
├── pyproject.toml
├── src/
│   ├── grid_search/
│   │   ├── algorithms/
│   │   ├── api/
│   │   ├── benchmarks/
│   │   ├── generators/
│   │   ├── models/
│   │   └── ...
│   └── scripts/
└── tests/
```

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e ".[dev]"
```

---

## Running Tests

```bash
pytest
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

## Running the API

Start the development server:

```bash
uvicorn grid_search.api.app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to access the automatically generated OpenAPI documentation.

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

### In Progress

- FastAPI backend
- Interactive frontend
- Search visualisation and animation

### Planned

- Weighted terrain
- Additional search algorithms
- Maze generation
- Live algorithm visualisation
- Performance optimisations
- Comparison of alternative graph representations

---

## License

This project is intended as a learning project for exploring graph search algorithms, software architecture, benchmarking, and interactive algorithm visualisation.
