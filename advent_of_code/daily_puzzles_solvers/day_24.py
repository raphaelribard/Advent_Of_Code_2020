"""
This module solves the day 24 puzzles.
"""
import numpy as np

ADJACENT_TILES_MOVES = np.array([[0, -2],
                                 [1, -1],
                                 [1, 1],
                                 [0, 2],
                                 [-1, 1],
                                 [-1,-1]])

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
    result:         Dictionary - The answers to the puzzle
    """
    day_24_data = day_24_data.split('\n')
    black_tiles = get_black_tiles(day_24_data)
    solutions = {'Part 1': black_tiles.shape[0]}

    solutions_dict = {}
    for day in range(100):
      black_tiles = get_new_black_tiles_set(black_tiles)
      solutions_dict[f'Day {day+1}'] = black_tiles.shape[0]
      if (day+1)%10 == 0:
        print(f'Day {day+1}: {black_tiles.shape[0]}')
    solutions['Part 2'] = solutions_dict['Day 100']
    return solutions

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
  tiles = np.array(tiles)
  # print(tiles)
  return tiles

def get_black_tiles(read_data):
  tiles = get_tiles(read_data)  
  counts = []
  unique_tiles = []
  unique_tiles_array = []
  for row in tiles:
    if str(row) in unique_tiles:
      pass
    else:
      count = len(np.where([np.array_equal(row, tiles[i,:]) for i in range(tiles.shape[0])])[0])
      unique_tiles.append(str(row))
      unique_tiles_array.append(list(row))
      counts.append(count) 
  counts = np.array(counts)
  black_indices = np.where(counts%2 == 1)[0]
  unique_tiles_array = np.array(unique_tiles_array)
  black_tiles = unique_tiles_array[black_indices]
  print(f'The number of black tiles is: {black_tiles.shape[0]}')

  return black_tiles

def get_adjacent_tiles(tile):
  return tile + ADJACENT_TILES_MOVES

def get_common_rows(A,B):
    nrows, ncols = A.shape
    dtype={'names':['f{}'.format(i) for i in range(ncols)],
           'formats':ncols * [A.dtype]}
    C = np.intersect1d(A.view(dtype), B.view(dtype))
    return C.view(A.dtype).reshape(-1, ncols)
  
def get_unique_rows(A,B):
    nrows, ncols = A.shape
    dtype={'names':['f{}'.format(i) for i in range(ncols)],
           'formats':ncols * [A.dtype]}
    C = np.setdiff1d(A.view(dtype), B.view(dtype))
    return C.view(A.dtype).reshape(-1, ncols)

def get_adjacent_black_tiles(tile, black_tiles):
  adjacent_tiles = get_adjacent_tiles(tile)
  return get_common_rows(adjacent_tiles, black_tiles)

def get_adjacent_white_tiles(tile, black_tiles):
  adjacent_tiles = get_adjacent_tiles(tile)
  adjacent_black_tiles = get_adjacent_black_tiles(tile, black_tiles)
  adjacent_white_tiles = get_unique_rows(adjacent_tiles,
                                         adjacent_black_tiles)
  return adjacent_white_tiles

def get_nb_of_adjacent_black_tiles(tile, black_tiles):
  adjacent_black_tiles = get_adjacent_black_tiles(tile, black_tiles)
  return adjacent_black_tiles.shape[0]

def get_new_black_tiles_set(black_tiles):
  black_tiles_to_keep = []
  white_tiles_to_flip = []

  for black_tile in black_tiles:
    adjacent_black_tiles = get_nb_of_adjacent_black_tiles(black_tile, black_tiles)
    if adjacent_black_tiles in [1, 2]:
      black_tiles_to_keep.append(list(black_tile))
    adjacent_white_tiles = get_adjacent_white_tiles(black_tile, black_tiles)
    for adjacent_white_tile in adjacent_white_tiles:
      if list(adjacent_white_tile) not in white_tiles_to_flip:
        adjacent_black_tiles = get_nb_of_adjacent_black_tiles(adjacent_white_tile,
                                                              black_tiles)
        if adjacent_black_tiles == 2:
          white_tiles_to_flip.append(list(adjacent_white_tile))
  black_tiles_to_keep = np.array(black_tiles_to_keep)
  white_tiles_to_flip = np.array(white_tiles_to_flip)
  black_tiles = np.concatenate([black_tiles_to_keep,
                                white_tiles_to_flip])
  return black_tiles
