"""
-Use divide and conquer to generate random quadrants
-For now, only have 1 difficulty.
-This difficulty generates quadrants with [4-7] numbers
-Eventually Google "how to tell if a Sudoku grid is solvable"
for the issue of making sure that the final grid we generate is 
actually doable lol
"""

import numpy as np
from sudoku import Sudoku




class SudokuGenerator(Sudoku):


    # Indicate how large of a board is desired.
    # A quad_row/col is just a column of quadrants.
    # A standard sud board is 3x3 for example
    def __init__(self, quad_rows = 3, quad_cols = 3):
        self.quad_rows = quad_rows
        self.quad_cols = quad_cols
        self.quad_rows = 3
        self.quad_cols = 3

        self.grid = np.full((9,9), 0) 

    def gen_quad(self):
        size = (3,3)
        a = list(range(0,10))
        quad_gen = lambda probs: np.random.choice(a, size = size, p = probs)
        probs = [.55, .05, .05, .05, .05, .05, .05, .05, .05, .05]
        # TODO: make the probs be not static and determined by a difficulty

        quad = quad_gen(probs)
        while not self.quad_valid(quad):
            quad = quad_gen(probs)


        quad = quad.astype("int")
        return quad


    def quad_valid(self, quad):
        return np.count_nonzero(np.unique(quad)) == np.count_nonzero(quad)


    # Make sure that all 3 rows and all 3 cols of a quad are compliant w the 
    # rest of the grid
    def check_compliance(self, curr_beg_row, curr_beg_col):
        for i in range(3):
            row = self.grid[curr_beg_row + i, :]
            col = self.grid[:, curr_beg_col + i]
            if self.row_col_valid(row) and self.row_col_valid(col):
                return True
        return False


    # Line can be either a row or a col
    def row_col_valid(self, line):
        return len(line.nonzero()[0]) == len(np.unique(line.take(
               line.nonzero()[0])))
     


    # Iteratively put in neq quads to the grid that fit
    def generate(self):
        quads_genned = 0
        while quads_genned < 9:
            quad = self.gen_quad()
            curr_beg_row = quads_genned // self.quad_rows
            curr_beg_col = quads_genned % self.quad_cols


            self.grid[curr_beg_row:curr_beg_row + 3,    
                      curr_beg_col: curr_beg_col + 3] = quad

            if self.check_compliance(curr_beg_row, curr_beg_col):
                print(quad)
                quads_genned += 1
        return self.grid
        
"""
sud_gen = SudokuGenerator()

sud_gen.generate()
sud_gen.print_grid()
print(sud_gen.grid)
"""
