import numpy as np
from sudoku import Sudoku


missing_3 = np.array([[0,3,2,5,6,7,9,4,8],
                      [5,4,6,3,8,9,2,1,7],
                      [9,7,8,2,4,1,6,3,5],
                      [2,0,4,9,1,8,7,5,3],
                      [7,1,5,6,3,2,8,9,4],
                      [3,8,9,4,7,5,1,2,6],
                      [8,5,7,1,2,3,4,6,9],
                      [6,9,1,7,5,4,3,8,2],
                      [4,2,3,8,9,6,5,7,0]])


class SudokuSolver(Sudoku):

    def __init__(self, grid):
        self.empty_val = 0 # value i use to signify a cell aint filled in
        self.grid = grid
        # self.candidates = np.full((self.grid.shape[0], self.grid.shape[1]), 0)
        self.candidates = self.get_all_candidates() 

    def solve(self):
        pass


    def get_all_candidates(self):
        candidates = np.empty((1,81))
        for row_index in range(9):
            for col_index in range(9):
                cell = self.grid[row_index,col_index]
                # if a cell is already filled, there's only 1 candidate
                if cell == self.empty_val:
                    candidates[row_index, col_index] = cell
                else:
                    candidates[row_index, col_index] =\
                        self.get_cell_candidates(row_index, col_index)


    def get_cell_candidates(self, row_index, col_index):
        candidates = np.array(range(1,10))

        for candidate in candidates:
            if not self.check_all(row_index, col_index, candidate):
                np.delete(candidates, np.where(candidates == candidate))

        return candidates



solv = SudokuSolver(missing_3)
print(solv.candidates[0,0])

