import unittest
import numpy as np
from sudoku_generator import SudokuGenerator
# Write tests for this class lol, this will make debugging MUCH easier.




class TestSudokuGenerator(unittest.TestCase):


    def setUp(self):
        self.gen = SudokuGenerator()        
        self.quad = self.gen.gen_quad()
        self.bad_quad1 = np.array([[3,4,3],
                                   [0,6,0],
                                   [1,5,8]])

        self.bad_quad2 = np.array([[3,4,3],
                                   [7,6,2],
                                   [1,5,8]])

        self.bad_quad3 = np.array([[0,0,5],
                                   [0,0,0],
                                   [5,0,0]])


        self.zer_quad = np.zeros((3,3)).astype("int")
        pass

    def test_gen_quad(self):
        self.assertTrue(np.count_nonzero(np.unique(self.quad)) == 
                        np.count_nonzero(self.quad))

    def test_sec_valid(self):
        self.assertFalse(self.gen.quad_valid(self.bad_quad1))
        self.assertFalse(self.gen.quad_valid(self.bad_quad2))
        self.assertFalse(self.gen.quad_valid(self.bad_quad3))
        self.assertTrue(self.gen.quad_valid(self.zer_quad))
        self.assertTrue(self.gen.quad_valid(self.quad))
        # GIVE ME SOME ROWS AND SOME COLUMNS TOO PLS!  


if __name__ == "__main__":
    unittest.main()
