"""
-Use divide and conquer to generate random quadrants
-Eventually Google "how to tell if a Sudoku grid is solvable"
for the issue of making sure that the final grid we generate is 
actually doable lol

"""

import numpy as np
from sudoku import Sudoku
from math import sqrt


class SquareError(BaseException):
    pass


class SudokuGenerator(Sudoku):

    # Indicate how large of a board is desired.
    # A quad_row/col is just a column of quadrants.
    # try to get a solution that works on a 4x4 board
    def __init__(self, difficulty, size = (4,4)):

        if size[0] != size[1] or sqrt(size[0]) != int(sqrt(size[0])):
            raise SquareError ("Your grid wouldn't be a square")
        diff_to_removals = {"e": np.arange(10,15), 
                            "m": np.arange(15,20), 
                            "h": np.arange(20,25)}

        self.chars_to_remove = np.random.choice(diff_to_removals[difficulty])

        self.quad_rows = quad_rows
        self.quad_cols = quad_cols

        self.quad_size = (sqrt(size[0]), sqrt(size[1]))

        self.edge_len = size[0]
        self.grid = np.full(size, 0) 

    def gen_quad(self, bad_quads = None):

        while True:
            quad = np.arange(1,)
            np.random.shuffle(quad)
            quad = quad.reshape((3,3))
            return quad
            """
            if len(bad_quads) == 0:
                return quad
            elif not self.check_array_in(quad, bad_quads):
                return quad
            """
               

    # Confirms that a row, col, or quad (sec) is valid generation

    # The amount of nonzero digits in sec must be equal to the amount of 
    # nonzero uniquevalues in the sec.
    def sec_valid(self, sec):
        return np.count_nonzero(np.unique(sec)) == np.count_nonzero(sec)


    # Make sure that all 3 rows and all 3 cols of a quad are compliant w the 
    # rest of the grid
    def check_compliance(self, curr_beg_row, curr_beg_col):
        for i in range(3):
            row = self.grid[curr_beg_row + i, :]
            col = self.grid[:, curr_beg_col + i]
            if not self.sec_valid(row) or not self.sec_valid(col):
                return False
        return True


    # Iteratively put in neq quads to the grid that fit
    def generate(self):
        quads_genned = 0
        # bad_quads = []
        while quads_genned < 9:
            curr_beg_row = (quads_genned // self.quad_rows) * 3
            curr_beg_col = (quads_genned % self.quad_cols) * 3
            self.print_grid()
            """
            if quads_genned == 8:
                self.generate_final_quad(quads_genned, curr_beg_row, 
                                         curr_beg_col)
            """
            quad = self.gen_quad()

            self.grid[curr_beg_row: curr_beg_row + 3,    
                      curr_beg_col: curr_beg_col + 3] = quad

            if self.check_compliance(curr_beg_row, curr_beg_col):
                # bad_quads = []
                quads_genned += 1

            # else:
              #  bad_quads.append(quad)


        return self.grid


    def check_array_in(self, arr_to_check, population):
        for array in population:
            if np.array_equal(arr_to_check, array):
                return True
        return False


    def generate_final_quad(self, beg_row, beg_col):
        quad = np.arange(1,10).reshape((3,3))
        for num in range(1,10):
            # find where num goes
            pass


        

sud_gen = SudokuGenerator("e", (4,4))
print(sud_gen.generate())


