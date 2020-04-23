import numpy as np
import unittest
import sudoku
np.random.seed(0) # For reproducability


def empty_grid():
    return np.full((9,9), 0)


def all_unique_grid():
    return np.random.rand(9,9)


test_grid_1 = empty_grid()
test_grid_1[8,8] = 3


g1 = sudoku.Sudoku()
g1.make_guess(9,9,3)

np.testing.assert_array_equal(g1.grid, test_grid_1)



# Probably will have to use unittest module down here (or in a diff
# file) just so I can have access to assertTrue, assertFalse, etc.
# It doesn't look like numpy has methods like that. 

