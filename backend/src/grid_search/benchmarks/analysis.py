import pandas as pd


def load_results(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def average_runtime(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(
            [
                "scenario",
                "algorithm",
                "grid_size",
            ]
        )["runtime_ms"]
        .mean()
        .reset_index()
    )


def average_nodes_expanded(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(
            [
                "scenario",
                "algorithm",
                "grid_size",
            ]
        )["nodes_expanded"]
        .mean()
        .reset_index()
    )


def average_path_length(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(
            [
                "scenario",
                "algorithm",
                "grid_size",
            ]
        )["path_length"]
        .mean()
        .reset_index()
    )
