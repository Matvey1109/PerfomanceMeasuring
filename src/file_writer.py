class FileWriter:
    """Class to handle file writing operation"""

    @staticmethod
    def write_benchmark_output(output: str, file_path: str) -> None:
        """Format and write the benchmark output into Markdown file"""
        lines: list[str] = output.splitlines()
        formatted: list[str] = [
            "| Test Name | Min Time (us) | Max Time (us) | Mean Time (us) | StdDev (us) | Median Time (us) | IQR | OPS | Rounds |"
        ]
        formatted.append(
            "|-----------|---------------|---------------|----------------|-------------|-----------------|-----|-----|-------|"
        )

        is_parsing: bool = False
        for line in lines:
            if line.startswith("Name (time in us)"):
                is_parsing = True
                continue
            if is_parsing and line.strip() == "":
                is_parsing = False
                break
            if is_parsing:
                parts: list[str] = [p.strip() for p in line.split() if p.strip()]
                if len(parts) >= 10:
                    formatted.append(
                        f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} | {parts[-3]} | {parts[-2]} |"
                    )

        formatted_output: str = "\n".join(formatted)

        with open(file_path, "w") as f:
            f.write("# Benchmark Statistics\n\n")
            f.write("## Results from Benchmark Tests\n\n")
            f.write(formatted_output)
