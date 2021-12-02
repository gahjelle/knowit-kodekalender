"""Tests for AoC 2, 2021: Reisegodtgjørelse"""

# Standard library imports
import pathlib

# Third party imports
import knowit202102
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return knowit202102.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        (-121.655555555, 36.677777777),
        (51.416666666, 35.7),
        (6.772380555, 51.231144444),
    ]


def test_example1(example1):
    """Test solution on example input 1"""
    assert knowit202102.solution(example1) == 26094
