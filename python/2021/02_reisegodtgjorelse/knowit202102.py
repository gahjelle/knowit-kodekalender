"""KnowIt luke 2, 2021: Reisegodtgjørelse"""

# Standard library imports
import pathlib
import sys

# Third-party libraries
import numpy as np
import parse

# Pattern used to parse each line in the CSV file
POINT_PATTERN = parse.compile("{city},Point({lon:f} {lat:f})")

# Approximate radius of Earth in kilometers
EARTH_DIAMETER = 6371 * 2


def parse(puzzle_input):
    """Parse input"""
    return [
        (pos["lon"], pos["lat"])
        for line in puzzle_input.split("\n")
        if (pos := POINT_PATTERN.parse(line))
    ]


def solution(data):
    """Solve the puzzle"""
    current_pos = np.radians([0, 90])
    all_pos = np.radians(np.array(data))

    total_distance = 0
    while len(all_pos):
        distances = distance(
            current_pos[0], current_pos[1], all_pos[:, 0], all_pos[:, 1]
        )
        closest_idx = np.argmin(distances)
        total_distance += distances[closest_idx]
        current_pos = all_pos[closest_idx]
        all_pos = np.concatenate([all_pos[:closest_idx], all_pos[closest_idx + 1 :]])

    # Go back home at the end
    total_distance += distance(0, np.radians(90), current_pos[0], current_pos[1])

    return round(total_distance)


def distance(λ1, ϕ1, λ2, ϕ2):
    """Compute distance with the haversine formula"""
    return EARTH_DIAMETER * np.arcsin(
        np.sqrt(
            np.sin((ϕ2 - ϕ1) / 2) ** 2
            + np.cos(ϕ1) * np.cos(ϕ2) * np.sin((λ2 - λ1) / 2) ** 2
        )
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    return solution(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        print(solve(puzzle_input=pathlib.Path(path).read_text().strip()))
