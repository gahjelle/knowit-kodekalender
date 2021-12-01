"""Tests for AoC 1, 2021: Talltull"""

# Standard library imports
import pathlib

# Third party imports
import knowit202101
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return knowit202101.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return knowit202101.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [1, 2, 3, 4, 5]


def test_example1(example1):
    """Test solution on example input 1"""
    assert knowit202101.solution(example1) == 15


def test_example2(example2):
    """Test solution on example input 2"""
    assert knowit202101.solution(example2) == 99
