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

    # Indicate desired board size.
    # A quad_row/col is just a column of quadrants.
    # try to get a solution that works on a 4x4 board
    def __init__(self, difficulty, size = (9,9)):

        if size[0] != size[1] or sqrt(size[0]) != int(sqrt(size[0])):
            raise SquareError ("Your grid wouldn't be a square")
        diff_to_removals = {"e": np.arange(10,15), 
                            "m": np.arange(15,20), 
                            "h": np.arange(20,25)}

        self.chars_to_remove = np.random.choice(diff_to_removals[difficulty])



        self.edge_len = size[0]
        self.sqrt_edge_len = int(sqrt(size[0]))
        self.grid = np.full(size, 0) 


    def gen_row(self, bad_rows = None):

        while True:
            row = np.arange(1,self.edge_len + 1)
            np.random.shuffle(row)
            return row

            """
            if len(bad_quads) == 0:
                return quad
            elif not self.check_array_in(quad, bad_quads):
                return quad
            """
               

    # Confirm that a row, col, or quad (sec) is valid generation
    # The amount of nonzero digits in sec must be equal to the amount of 
    # nonzero uniquevalues in the sec.
    # A "sec" can be good if it contains multiple zeros but all nonzeros
    # are unique
    def sec_valid(self, sec):
        return np.count_nonzero(np.unique(sec)) == np.count_nonzero(sec)


    # Make sure that all 9 cols of a row are compliant w the rest of the grid
    def check_row_compliance(self):
        for col_index in range(self.edge_len):
            col = self.grid[:, col_index]
            if not self.sec_valid(col):
                return False
        return True


    # checks all quads in a given row
    def check_row_quads(self, rows_genned):
        curr_beg_row = (rows_genned // self.sqrt_edge_len) * self.sqrt_edge_len
        for i in range(self.sqrt_edge_len):
            curr_beg_col = i * self.sqrt_edge_len
            quad = self.grid[curr_beg_row:curr_beg_row + self.sqrt_edge_len, 
                             curr_beg_col:curr_beg_col + self.sqrt_edge_len]
            if not self.sec_valid(quad):
                return False
        return True

    def list_possibilities(self, rows_genned):
        upper_bnd_row_index = rows_genned - 1
        all_possibilities = []
        for col_index in range(0,self.edge_len):
            poss = self.spot_possibilities(upper_bnd_row_index, col_index)
            all_possibilities.append(poss)
        return all_possibilities

            
    # Find all posibilities that a spot at row_index, col_index could contain
    def spot_possibilities(self, row_index, col_index):
        all_poss = set(range(1,10))
        col_so_far = set(self.grid[:row_index, col_index])
        beg_row_index = self.get_beg_index(row_index)
        beg_col_index = self.get_beg_index(col_index)
        quad_so_far = self.grid[beg_row_index:beg_row_index + 3,
                                beg_col_index:beg_col_index + 3].flatten()
        quad_no_zeros = set(quad_so_far[np.nonzero(quad_so_far)])
        elim_poss = col_so_far.union(quad_no_zeros)
        poss_left = all_poss - elim_poss
        return poss_left
        


    # Iteratively put in new rows that fit
    def generate(self):
        rows_genned = 0
        # bad_rows = []
        while rows_genned < self.edge_len:
            print(self.grid,"\n")
            print(self.list_possibilities(rows_genned))
            row = self.gen_row()
            self.grid[rows_genned, :] = row

            if self.check_row_compliance() and\
               self.check_row_quads(rows_genned):
                # bad_quads = []
                rows_genned += 1

            # else:
              #  bad_quads.append(quad)


        return self.grid


    def check_array_in(self, arr_to_check, population):
        for array in population:
            if np.array_equal(arr_to_check, array):
                return True
        return False


sud_gen = SudokuGenerator("e", (9,9))
print(sud_gen.generate())


