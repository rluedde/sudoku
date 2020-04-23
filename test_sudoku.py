import numpy as np
import unittest
import sudoku
np.random.seed(0) # For reproducability


def empty_grid():
    return np.full((9,9), 0)


def all_unique_grid():
    return np.random.rand(9,9)


class TestSudoku(unittest.TestCase):

    # Two instances of Sudoku
    g1 = sudoku.Sudoku() # g1's grid will be all non-unique by default
    u1 = sudoku.Sudoku()

    u1.grid = all_unique_grid() # every element in u1 is now unique

    def test_make_guess(self):
        # Make sure normal guess works
        test_grid = empty_grid()
        test_grid[6,2] = 3
        np.testing.assert_array_equal(self.g1.make_guess(6,2,3), test_grid)

        # Make sure guess of 9 works
        test_grid = empty_grid()
        self.g1.grid = empty_grid()
        test_grid[3,4] = 9
        np.testing.assert_array_equal(self.g1.make_guess(3,4,9), test_grid)

        # Make sure certain guesses are prevented
        self.assertRaises(Exception, self.g1.make_guess, -1,-1, 3) # No neg. indexing
        self.assertRaises(Exception, self.g1.make_guess, 9, 9, 3) # 9 isn't valid index 
        self.assertRaises(Exception, self.g1.make_guess, 8, 8, 19) # 0 < guess =< 9
        self.assertRaises(Exception, self.g1.make_guess, 3, 5, "13") # No str
        self.assertRaises(Exception, self.g1.make_guess, 3, 5, 0) # No zero guess 
     
        # Make sure that print_grid() doesn't raise an Exception
        try:
            self.g1.print_grid()
        except:
            self.fail("print_grid() raised an an Exception unexpectedly!")

    def test_col_clear(self):
        # self.assertFalse(self.g1.col_clear(3))
        # self.assertTrue(self.g1.col_clear(3))
        pass


# Allows us to run at command line without extra cmd args
if __name__ == "__main__":
    unittest.main()
