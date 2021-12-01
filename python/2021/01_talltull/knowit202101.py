"""KnowIt luke 1, 2021: Talltull"""

# Standard library imports
import pathlib
import sys

NUMBERS = [
    ("en", 1),
    ("to", 2),
    ("tre", 3),
    ("fire", 4),
    ("fem", 5),
    ("seks", 6),
    ("sju", 7),
    ("åtte", 8),
    ("ni", 9),
    ("ti", 10),
    ("elleve", 11),
    ("tolv", 12),
    ("tretten", 13),
    ("fjorten", 14),
    ("femten", 15),
    ("seksten", 16),
    ("sytten", 17),
    ("atten", 18),
    ("nitten", 19),
    ("tjue", 20),
    ("tretti", 30),
    ("førti", 40),
    ("femti", 50),
]


def parse(puzzle_input):
    """Parse input

    >>> parse("førtifire")
    [40, 4]

    >>> parse("entrettinittento")
    [1, 30, 19, 2]

    >>> parse("femti")
    [50]
    """
    numbers = []
    while puzzle_input:
        for number, value in NUMBERS[::-1]:
            if puzzle_input.startswith(number):
                puzzle_input = puzzle_input.removeprefix(number)
                numbers.append(value)
                break

    return numbers


def solution(data):
    """Solve the puzzle"""
    return sum(data)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    return solution(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        print(solve(puzzle_input=pathlib.Path(path).read_text().strip()))
