"""
This module unit tests the day 1 solver.
"""
from advent_of_code.daily_puzzles_solvers.day_1 import day_1_puzzle_solve

def test_day_1_puzzle_solve():
    """
    test_day_1_puzzle_solve unit tests the day 1 solver given the example.
    """
    with open('tests/test_data/day_1_part_1_test.txt') as local_file:
        read_data = local_file.read()
    example_result = day_1_puzzle_solve(read_data)
    print(example_result)
    assert example_result == 514579
