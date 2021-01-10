"""
This module provides a Solver class which can load the data located in the Data folder.
This Solver class will be able to solve the daily puzzles using class methods.
"""

from advent_of_code.daily_puzzles_solvers.day_1 import day_1_puzzle_solve

class Solver():
    """
    This defines the Solver class which gives the user methods to automagically load the data
    and solve the daily puzzles.
    """
    def __init__(self, data_path='Data/'):
        self.data_path = data_path
        self.data = {}
        self.available_days = []
        self.solutions = {}

    def __repr__(self):
        days = ''.join([4*" " + f"- Day {day}\n" for day in self.available_days])
        return  f"The data path is {self.data_path}.\n"\
                f"The available days are:\n{days}."

    def load_data(self):
        """
        load_data
        Simple class method to automagically load the data located in the Data folder.
        """
        data_dict = {}
        available_days = []
        for day in range(1, 25):
            try:
                for part in range(1, 3):
                    with open(f'{self.data_path}Day_{day}_part_{part}.txt') as local_file:
                        read_data = local_file.read()
                    data_dict[f'Day_{day}_part_{part}'] = read_data
                    available_days.append(day)
            except FileNotFoundError as exception:
                print(f"No file for day {day}: {exception}")
        self.data = data_dict
        self.available_days = set(available_days)
    
    def solve_day_1(self):
        """
        solve_day_1:    This function appends the day 1 result
                        to the solutions class attribute (dictionary)
        """
        part_1_result = day_1_puzzle_solve(self.data['Day_1_part_1'])
        self.solutions['day_1_part_1'] = part_1_result
    

test = Solver()
test.load_data()
test.solve_day_1()
print(test)
print(test.solutions)
# print(test.data['Day_1_part_1'])
# print(test.data['Day_2_part_1'])
