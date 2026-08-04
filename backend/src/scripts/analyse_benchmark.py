from grid_search.benchmarks.analysis import (
    average_nodes_expanded,
    average_path_length,
    average_runtime,
    load_results,
)


def main():
    df = load_results("benchmark_results.csv")

    print("Runtime averages")
    print(average_runtime(df))

    print("\nNodes expanded averages")
    print(average_nodes_expanded(df))

    print("\nAverage path length")
    print(average_path_length(df))

    print("\nAlgorithms tested")
    print(df["algorithm"].unique())

    print("\nScenarios tested")
    print(df["scenario"].unique())

    print("\nRuns per algorithm")
    print(df.groupby(["algorithm", "scenario", "grid_size"]).size())

    print("\nSuccess rate")
    print(df.groupby(["algorithm", "scenario", "grid_size"])["path_found"].mean())


if __name__ == "__main__":
    main()
