import numpy as np
import unittest
from sudoku import Sudoku
np.random.seed(0) # For reproducability


def empty_grid():
    return np.full((9,9), 0)


def unique_grid():
    return np.random.rand(9,9)


def complete_grid():
    complete_grid = np.array([[1,3,2,5,6,7,9,4,8],
                              [5,4,6,3,8,9,2,1,7],
                              [9,7,8,2,4,1,6,3,5],
                              [2,6,4,9,1,8,7,5,3],
                              [7,1,5,6,3,2,8,9,4],
                              [3,8,9,4,7,5,1,2,6],
                              [8,5,7,1,2,3,4,6,9],
                              [6,9,1,7,5,4,3,8,2],
                              [4,2,3,8,9,6,5,7,1]])
    return complete_grid


# Grid is missing 3 elements at:
# [0,0], [3,1], [8,8]
def missing_3():
    missing_3 = np.array([[0,3,2,5,6,7,9,4,8],
                          [5,4,6,3,8,9,2,1,7],
                          [9,7,8,2,4,1,6,3,5],
                          [2,0,4,9,1,8,7,5,3],
                          [7,1,5,6,3,2,8,9,4],
                          [3,8,9,4,7,5,1,2,6],
                          [8,5,7,1,2,3,4,6,9],
                          [6,9,1,7,5,4,3,8,2],
                          [4,2,3,8,9,6,5,7,0]])
    return missing_3


# Grid is missing 1 element at:
# [5,6] - the valid guess is a 1
def missing_1():
    missing_1 = np.array([[1,3,2,5,6,7,9,4,8],
                          [5,4,6,3,8,9,2,1,7],
                          [9,7,8,2,4,1,6,3,5],
                          [2,6,4,9,1,8,7,5,3],
                          [7,1,5,6,3,2,8,9,4],
                          [3,8,9,4,7,5,0,2,6],
                          [8,5,7,1,2,3,4,6,9],
                          [6,9,1,7,5,4,3,8,2],
                          [4,2,3,8,9,6,5,7,1]])
    return missing_3


class TestSudoku(unittest.TestCase):

    
    # Set up variables that will be needed for tests
    def setUp(self):
        self.zero_arr = empty_grid()
        self.complete_arr = complete_grid()
        self.missing_1_arr = missing_1()
        self.g = Sudoku() # Homogenous grid
        self.u = Sudoku() # All-unique grid
        self.c = Sudoku() # Valid, complete grid
        self.t = Sudoku() # Partially complete grid - missing 3 #s
        self.o = Sudoku() # Partially complete grid - missing 1 #
        self.u.grid = unique_grid()
        self.c.grid = complete_grid() 
        self.t.grid = missing_3()
        self.o.grid = missing_1()


    def test_print_grid(self):
        
        # Make sure that print_grid() doesn't raise an Exception
        try:
            print("\ntest print_grid():")
            self.c.print_grid()
        except:
            self.fail("print_grid() raised an an Exception unexpectedly!")


    def test_make_guess(self):
        # Note: Lots of data mutability situations arise in this test.

        # Make sure normal guess works
        self.zero_arr[6,2] = 3
        np.testing.assert_array_equal(self.g.make_guess(6,2,3), self.zero_arr)

        # Make sure guess of 9 works
        self.zero_arr[3,4] = 9
        np.testing.assert_array_equal(self.g.make_guess(3,4,9), self.zero_arr)

        # Make sure certain guesses are prevented
        self.assertRaises(Exception, self.g.make_guess, -1,-1, 3) # No neg. index
        self.assertRaises(Exception, self.g.make_guess, 9, 9, 3) # 9 isn't valid 
        self.assertRaises(Exception, self.g.make_guess, 8, 8, 19) # 0<guess<=9
        self.assertRaises(Exception, self.g.make_guess, 3, 5, "13") # No str
        self.assertRaises(Exception, self.g.make_guess, 3, 5, 0) # No zero guess 
    

        # Make sure current numbers can't be changed
        np.testing.assert_array_equal(complete_grid(),
                                      self.c.make_guess(2,3,3))

        # Make sure that an element that's a 0 can be changed
        np.testing.assert_raises(AssertionError, assert_array_equal,
                                 empty_grid(), 
                                 self.z.make_guess(4,7,4))


        # Make sure that guess is valid
        # This test gives an invalid guess so make_guess should return 
        # the grid before the guess was made.j
        np.testing.assert_array_equal(missing_1_grid(), 
                                      self.o.make_guess(5,6,8)


    def test_col_clear(self):

        self.assertTrue(self.u.col_clear(3))
        self.assertTrue(self.c.row_clear(2))
        self.assertFalse(self.g.col_clear(7))


    def test_row_clear(self):

        self.assertTrue(self.u.row_clear(6))
        self.assertTrue(self.c.row_clear(5))
        self.assertFalse(self.g.row_clear(1))


    def test_rows_cols_clear(self):

        self.assertTrue(self.u.rows_cols_clear())
        self.assertFalse(self.g.rows_cols_clear())
        self.assertTrue(self.c.rows_cols_clear())


    def test_quadrant_clear(self):
        
        self.assertTrue(self.u.quadrant_clear(0,0))
        self.assertTrue(self.c.quadrant_clear(0,0))
        self.assertTrue(self.c.quadrant_clear(0,3))
        self.assertTrue(self.c.quadrant_clear(3,3))
        self.assertTrue(self.c.quadrant_clear(3,6))
        self.assertFalse(self.g.quadrant_clear(6,6))


    def test_all_quadrants_clear(self):

        self.assertTrue(self.u.all_quadrants_clear())
        self.assertTrue(self.c.all_quadrants_clear())
        self.assertFalse(self.g.all_quadrants_clear())


    def test_all_clear(self):
        
        self.assertTrue(self.c.all_clear())
        self.assertTrue(self.u.all_clear())
        self.assertFalse(self.g.all_clear())


    def test_game_over(self):
        
        self.assertTrue(self.c.game_over())
        self.c.grid[3,4] = 0
        self.assertFalse(self.c.game_over())
        self.assertFalse(self.g.game_over())


# Allows us to run at command line without extra cmd args
if __name__ == "__main__":
    unittest.main()
