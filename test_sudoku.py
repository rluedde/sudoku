import numpy as np
import unittest
import sudoku

def empty_grid():
    return np.full((9,9), 0)

test_grid_1 = empty_grid()
test_grid_1[8,8] = 3


g1 = sudoku.Sudoku()
g1.make_guess(9,9,6)

np.testing.assert_array_equal(g1.grid, test_grid_1)


