from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def _prepare_summary(
    df: pd.DataFrame,
    metric: str,
    scenario: str,
) -> pd.DataFrame:
    return (
        df[df["scenario"] == scenario]
        .groupby(
            [
                "algorithm",
                "grid_size",
            ]
        )[metric]
        .mean()
        .reset_index()
    )


def _plot_metric(
    df: pd.DataFrame,
    scenario: str,
    metric: str,
    ylabel: str,
    title: str,
    filename: str,
    output_dir: Path,
    log_scale: bool = False,
) -> None:

    summary = _prepare_summary(
        df,
        metric,
        scenario,
    )

    plt.figure(figsize=(10, 6))

    sns.lineplot(
        data=summary,
        x="grid_size",
        y=metric,
        hue="algorithm",
        style="algorithm",
        markers=True,
    )

    if log_scale:
        plt.yscale("log")

    plt.xlabel("Grid Size")
    plt.ylabel(ylabel)
    plt.title(f"{title} ({scenario})")

    plt.grid(True)
    plt.tight_layout()

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_dir / filename,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


def plot_runtime(
    df: pd.DataFrame,
    scenario: str,
    output_dir: Path,
) -> None:
    _plot_metric(
        df,
        scenario,
        "runtime_ms",
        "Runtime (ms)",
        "Runtime vs Grid Size",
        f"runtime_{scenario}.png",
        output_dir,
        log_scale=True,
    )


def plot_nodes_expanded(
    df: pd.DataFrame,
    scenario: str,
    output_dir: Path,
) -> None:
    _plot_metric(
        df,
        scenario,
        "nodes_expanded",
        "Nodes Expanded",
        "Nodes Expanded vs Grid Size",
        f"nodes_expanded_{scenario}.png",
        output_dir,
    )


def plot_memory(
    df: pd.DataFrame,
    scenario: str,
    output_dir: Path,
) -> None:
    _plot_metric(
        df,
        scenario,
        "memory_bytes",
        "Memory (bytes)",
        "Memory Usage vs Grid Size",
        f"memory_{scenario}.png",
        output_dir,
        log_scale=True,
    )


def plot_path_length(
    df: pd.DataFrame,
    scenario: str,
    output_dir: Path,
) -> None:
    _plot_metric(
        df,
        scenario,
        "path_length",
        "Path Length",
        "Path Length vs Grid Size",
        f"path_length_{scenario}.png",
        output_dir,
    )
