import unittest
import numpy as np
from sudoku_generator import SudokuGenerator
# Write tests for this class lol, this will make debugging MUCH easier.




class TestSudokuGenerator(unittest.TestCase):


    def setUp(self):
        self.gen = SudokuGenerator()        
        self.quad = self.gen.gen_quad()
        # self.bad_quad = SOMETHING
        self.zer_quad = np.zeros((3,3)).astype("int")
        pass

    def test_gen_quad(self):
        self.assertTrue(np.count_nonzero(np.unique(self.quad)) == 
                        np.count_nonzero(self.quad))

    def test_quad_valid(self):
        # self.assertFalse(self.gen.quad_valid(self.bad_quad))
        self.assertTrue(self.gen.quad_valid(self.zer_quad))
        self.assertTrue(self.gen.quad_valid(self.quad))

    def test_check_compliance(self):
        pass

    def row_col_valid(self):
        pass



if __name__ == "__main__":
    unittest.main()
