import io
from contextlib import redirect_stdout

import pytest


def format_benchmark_output(output):
    """Format the benchmark output into a more readable Markdown structure."""
    lines = output.splitlines()
    formatted = [
        "| Test Name | Min Time (us) | Max Time (us) | Mean Time (us) | StdDev (us) | Median Time (us) | IQR | OPS | Rounds |"
    ]
    formatted.append(
        "|-----------|---------------|---------------|----------------|-------------|-----------------|-----|-----|-------|"
    )

    parsing = False
    for line in lines:
        if line.startswith("Name (time in us)"):
            parsing = True
            continue
        if parsing and line.strip() == "":
            parsing = False
            break
        if parsing:
            parts = [p.strip() for p in line.split() if p.strip()]
            if len(parts) >= 10:
                formatted.append(
                    f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} | {parts[-3]} | {parts[-2]} |"
                )

    return "\n".join(formatted)


def workflow():
    # Run benchmark tests and capture the output
    pytest_args = ["--benchmark-only"]
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        pytest.main(pytest_args)

    # Save captured benchmark results to a Markdown file
    output = buffer.getvalue()
    formatted_output = format_benchmark_output(output)

    with open("benchmark_statistics.md", "w") as f:
        f.write("# Benchmark Statistics\n\n")
        f.write("## Results from Benchmark Tests\n\n")
        f.write(formatted_output)

    print("Benchmark results saved to benchmark_statistics.md")
