import io
from contextlib import redirect_stdout

import pytest

from src.file_writer import FileWriter
from src.type_of_tests import TypeOfTests

STATISTICS_FILE_PATH = "results/benchmark_statistics.md"
HISTOGRAM_FILE_PATH = "results/benchmark_histogram"


def workflow() -> None:
    print("Program started")

    # Run benchmark tests and capture the output
    pytest_args: list[str] = [
        "-m",
        TypeOfTests.LIST_CREATION,
        "--benchmark-only",
        f"--benchmark-histogram={HISTOGRAM_FILE_PATH}",
    ]

    buffer: io.StringIO = io.StringIO()
    with redirect_stdout(buffer):
        pytest.main(pytest_args)

    # Save captured benchmark results to a Markdown file
    output: str = buffer.getvalue()
    FileWriter.write_benchmark_output(output, STATISTICS_FILE_PATH)

    print("Benchmark results saved to results/benchmark_statistics.md")
