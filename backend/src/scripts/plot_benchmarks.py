from pathlib import Path

from grid_search.benchmarks.analysis import load_results
from grid_search.benchmarks.plots import (
    plot_memory,
    plot_nodes_expanded,
    plot_path_length,
    plot_runtime,
)


def main():

    df = load_results("benchmark_results.csv")

    output_dir = Path("docs/benchmark_results")

    for scenario in [
        "open",
        "sparse",
        "dense",
    ]:
        plot_runtime(
            df,
            scenario,
            output_dir,
        )

        plot_nodes_expanded(
            df,
            scenario,
            output_dir,
        )

        plot_memory(
            df,
            scenario,
            output_dir,
        )

        plot_path_length(
            df,
            scenario,
            output_dir,
        )


if __name__ == "__main__":
    main()
