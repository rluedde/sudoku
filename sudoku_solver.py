import numpy as np
from sudoku import Sudoku
from time import sleep

sudoku =    np.array([[8, 1, 0, 0, 3, 0, 0, 2, 7], 
                      [0, 6, 2, 0, 5, 0, 0, 9, 0], 
                      [0, 7, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 9, 0, 6, 0, 0, 1, 0, 0], 
                      [1, 0, 0, 0, 2, 0, 0, 0, 4], 
                      [0, 0, 8, 0, 0, 5, 0, 7, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 8, 0], 
                      [0, 2, 0, 0, 1, 0, 7, 5, 0], 
                      [3, 8, 0, 0, 7, 0, 0, 4, 2]])



zeros = np.zeros((9,9), dtype = "int32")
class SudokuSolver(Sudoku):


    def __init__(self, grid):
        self.grid = grid
        self.spots_solved = 0 

        
    # Improvements:
    # -Go through and find all spots where the len(candidates) == 1
    #   fill in that 
    # cell and then go through and run the recursive backtracker?
    # -Keep track of trees more efficiently? 
    # -Xwing
    def solve(self, spots_solved = 0):
        self.print_grid()

        # This might work if you eliminate possibilities somehow
        if spots_solved == 81:
            return True

        row_index = self.get_row_index(spots_solved)
        col_index = self.get_col_index(spots_solved)

        if self.grid[row_index, col_index] == 0:

            candidates = self.get_cell_candidates(row_index, col_index)

            for candidate in candidates:
                self.grid[row_index, col_index] = candidate

                if self.solve(spots_solved + 1):
                    return True

                self.grid[row_index, col_index] = 0

        else:
            self.solve(spots_solved + 1)

        return False


    def get_row_index(self, spots_solved):
        return spots_solved // 9 


    def get_col_index(self, spots_solved):
        return spots_solved % 9


    # Get all of the possible values that a cell can take
    def get_cell_candidates(self, row_index, col_index):
        candidates = np.arange(1,10)
        if self.grid[row_index,col_index] != 0:
            return []
        for candidate in candidates:
            if not self.check_all(row_index, col_index, candidate):
                # Array version of list.remove():
                candidates = np.delete(candidates, 
                                       np.where(candidates == candidate))
        
        return candidates




solv = SudokuSolver(sudoku)
print(solv.solve())



