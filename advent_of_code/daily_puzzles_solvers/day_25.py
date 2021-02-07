"""
This module solves the day 25 puzzles.
"""
import numpy as np

def day_25_puzzle_solve(day_25_data):
    """
    day_25_puzzle_solve:
    This function solves the 2 parts of the Advent of Code 2020
    day 25 puzzle

    Parameters
    ----------
    day_25_data :    String - The raw data read from the input file.

    Returns
    -------
    result:         Dictionary - The answers to the puzzle
    """
    day_25_data = day_25_data.split('\n')
    day_25_data = [int(item) for item in day_25_data]
    day_25_data = {'card_pub': day_25_data[0],
                   'door_pub': day_25_data[1]}
    encryption_key = get_encryption_key(day_25_data['card_pub'],
                                        day_25_data['door_pub'])['encryption_key']
    solutions = {'Part 1': encryption_key}

    return solutions

def find_loop_size(end_value):
  value = 1
  subject_number = 7
  i=0

  while value!=end_value:
    value*=subject_number
    value = value%20201227
    i+=1
  return i

def get_value(subject_number, loop_size):
  value = 1
  for i in range(loop_size):
    value*=subject_number
    value = value%20201227
  return value

def get_encryption_key(card_pub, door_pub):
  door_loop_size = find_loop_size(door_pub)
  encryption_key = get_value(card_pub, door_loop_size)
  return {'encryption_key': encryption_key}
