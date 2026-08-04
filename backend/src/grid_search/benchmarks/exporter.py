import csv
from dataclasses import asdict

from grid_search.benchmarks.models import BenchmarkRecord


def export_csv(
    records: list[BenchmarkRecord],
    filename: str,
) -> None:

    if not records:
        return

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=asdict(records[0]).keys(),
        )

        writer.writeheader()

        for record in records:
            writer.writerow(asdict(record))
