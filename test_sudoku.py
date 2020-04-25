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
    

class TestSudoku(unittest.TestCase):

    
    # Set up variables that will be needed for tests
    def setUp(self):
        self.zer_arr = empty_grid()
        self.g = Sudoku() # Homogenous grid
        self.u = Sudoku() # All-unique grid - tbh not rly neccessary
        self.c = Sudoku() # Valid, complete Sudoku grid
        self.u.grid = unique_grid()
        self.c.grid = complete_grid() 


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
        self.zer_arr[6,2] = 3
        np.testing.assert_array_equal(self.g.make_guess(6,2,3), self.zer_arr)

        # Make sure guess of 9 works
        self.zer_arr[3,4] = 9
        np.testing.assert_array_equal(self.g.make_guess(3,4,9), self.zer_arr)

        # Make sure certain guesses are prevented
        self.assertRaises(Exception, self.g.make_guess, -1,-1, 3) # No neg. indexing
        self.assertRaises(Exception, self.g.make_guess, 9, 9, 3) # 9 isn't valid 
        self.assertRaises(Exception, self.g.make_guess, 8, 8, 19) # 0 < guess =< 9
        self.assertRaises(Exception, self.g.make_guess, 3, 5, "13") # No str
        self.assertRaises(Exception, self.g.make_guess, 3, 5, 0) # No zero guess 
     

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
        self.assertTrue(self.c.quadrant_clear(0,3))
        self.assertTrue(self.c.quadrant_clear(3,3))
        self.assertTrue(self.c.quadrant_clear(3,6))
        self.assertFalse(self.g.quadrant_clear(6,6))
        
    # Do all quadrants here


# Allows us to run at command line without extra cmd args
if __name__ == "__main__":
    unittest.main()
