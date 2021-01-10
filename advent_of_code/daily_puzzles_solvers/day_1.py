import numpy as np

def day_1_puzzle_solve(day_1_data):
    """
    day_1_puzzle_solve:
    This function solves the 2 parts of the Advent of Code 2020
    day 1 puzzle

    Parameters
    ----------
    day_1_data :    String - The raw data read from the input file.

    Returns
    -------
    result:         Integer - The answer to the puzzle
    """
    day_1_data = day_1_data.split('\n')
    day_1_data = np.array([int(number) for number in day_1_data])
    for number_1 in day_1_data:
        for number_2 in day_1_data:
            if number_1 != number_2:
                if number_1 + number_2 == 2020:
                    result = number_1 * number_2
    return result
