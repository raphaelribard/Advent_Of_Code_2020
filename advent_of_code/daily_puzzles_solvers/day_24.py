"""
This module solves the day 24 puzzles.
"""
import numpy as np

def day_24_puzzle_solve(day_24_data):
    """
    day_24_puzzle_solve:
    This function solves the 2 parts of the Advent of Code 2020
    day 24 puzzle

    Parameters
    ----------
    day_24_data :    String - The raw data read from the input file.

    Returns
    -------
    result:         Dictionqry - The answers to the puzzle
    """
    day_24_data = day_24_data.split('\n')
    result = get_black_tiles(day_24_data)
    return result

def get_tile_to_flip_coordinates(tile_moves):
  tile = [0, 0] #row, col
  cursor = 0
  while cursor < len(tile_moves):
    move = tile_moves[cursor]
    # print(move)
    if move == 'w':
        tile[1]-=2
        cursor+=1
    elif move == 'e':
        tile[1]+=2
        cursor+=1
    elif move == 'n':
      tile[0]+=1
      if tile_moves[cursor + 1] == 'w':
        tile[1]-=1
        cursor+=2
      elif tile_moves[cursor + 1] == 'e':
        tile[1]+=1
        cursor+=2
    elif move == 's':
      tile[0]-=1
      if tile_moves[cursor + 1] == 'w':
        tile[1]-=1
        cursor+=2
      elif tile_moves[cursor + 1] == 'e':
        tile[1]+=1
        cursor+=2
  return tile

def get_tiles(read_data):
  tiles = []
  for tile_move in read_data:
    tiles.append(get_tile_to_flip_coordinates(tile_move))
  # print(tiles)
  # tiles = np.array([str(tile[0])+str(tile[1]) for tile in tiles])
  tiles = np.array(tiles)
  # print(tiles)
  return tiles

def get_black_tiles(read_data):
  tiles = get_tiles(read_data)
  # unique, frequency = np.unique(tiles,  
  #                             return_counts = True)  
  counts = []
  unique_tiles = []
  for row in tiles:
    if str(row) in unique_tiles:
      pass
    else:
      count = len(np.where([np.array_equal(row, tiles[i,:]) for i in range(tiles.shape[0])])[0])
      unique_tiles.append(str(row))
      counts.append(count) 
  counts = np.array(counts)
  black_tiles = np.sum(counts%2)
  print(f'The number of black tiles is: {black_tiles}')
  
  return black_tiles