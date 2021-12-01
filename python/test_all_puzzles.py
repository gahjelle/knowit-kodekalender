#!/usr/bin/env python
"""Test outputs of Advent of Code puzzle solutions"""

# Standard library imports
import importlib
import pathlib

# Third party imports
import pytest
from codetiming import Timer

PUZZLE_DIR = pathlib.Path(__file__).parent
PUZZLE_PATHS = sorted(p.parent for p in PUZZLE_DIR.rglob("**/output.py.txt"))


class TimingsLog:
    """Logger that can write timings to file"""

    time_units = (("m", 60), ("s", 1), ("ms", 1e-3), ("μs", 1e-6), ("ns", 1e-9))
    fmt_header = (
        "\n## {year}\n\n" "| Day | Puzzle | Python | Time |\n|:---|:---|:---|---:|\n"
    )
    fmt_entry = "| {day} | {puzzle} | {link} | {solution} |\n"

    def __init__(self, path):
        """Initialize logger"""
        self.path = path
        self.path.write_text("# KnowIt Kodekalender\n")
        self.current_year = 0

    def write_log(self, year, day, puzzle, link, solution):
        """Write an entry in the log"""
        if year != self.current_year:
            self.current_year = year
            self.write_line(self.fmt_header.format(year=year))

        self.write_line(
            self.fmt_entry.format(
                day=day,
                puzzle=puzzle,
                link=link,
                solution=self.prettytime(solution),
            )
        )

    def write_line(self, line):
        """Write one line to the log file"""
        with self.path.open(mode="a") as fid:
            fid.write(line)

    @classmethod
    def prettytime(cls, seconds):
        """Pretty-print number of seconds"""
        for unit, threshold in cls.time_units:
            if seconds > threshold:
                return f"{seconds / threshold:.3f} {unit}"


TIMINGS_LOG = TimingsLog(PUZZLE_DIR / "timings.py.md")


@pytest.mark.parametrize(
    "puzzle_path", PUZZLE_PATHS, ids=[p.name for p in PUZZLE_PATHS]
)
def test_puzzle(puzzle_path):
    """Test one puzzle against the expected solution"""

    # Import puzzle
    *_, year, puzzle = puzzle_path.parts
    day = puzzle[:2]
    puzzle_mod = importlib.import_module(f"{year}.{puzzle}.knowit{year}{day}")

    # Parse data
    puzzle_input = (puzzle_path / "input.txt").read_text().strip()
    puzzle_parse = getattr(puzzle_mod, "parse")
    puzzle_data = puzzle_parse(puzzle_input)

    # Solve the puzzle
    puzzle_func = getattr(puzzle_mod, "solution")
    with Timer(logger=None) as timer:
        solution = puzzle_func(puzzle_data)

    # Compare to expected output
    actual = [str(solution)]
    expected = (puzzle_path / "output.py.txt").read_text().strip().split("\n")[-1:]
    assert actual == expected

    # Log elapsed time
    puzzle_name = puzzle[3:].replace("_", " ").title()
    link = f"[knowit{year}{day}.py]({puzzle}/knowit{year}{day}.py)"
    TIMINGS_LOG.write_log(
        year=year,
        day=int(day),
        puzzle=puzzle_name,
        link=link,
        solution=timer.last,
    )
