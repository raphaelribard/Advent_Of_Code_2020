from daily_puzzles_solvers.day_1 import day_1_puzzle_solve

def test_day_1_puzzle_solve():
    with open('test_data/day_1_part_1_test.txt') as local_file:
        read_data = local_file.read()
    print(day_1_puzzle_solve(read_data))