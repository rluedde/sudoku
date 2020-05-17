import numpy as np
from sudoku import Sudoku


missing_3 = np.array([[0,3,2,5,6,7,9,4,8],
                      [5,4,6,3,8,9,2,1,7],
                      [9,7,8,2,4,1,6,3,5],
                      [2,0,4,9,1,8,7,5,3],
                      [7,1,5,6,3,2,8,9,4],
                      [3,8,9,4,0,5,1,2,6],
                      [8,5,7,0,2,3,4,6,9],
                      [6,9,1,0,5,4,3,8,2],
                      [4,2,3,8,9,6,5,7,0]])


class SudokuSolver(Sudoku):


    def __init__(self, grid):
        self.grid = grid
        self.spots_solved = 0
        self.tried_elements = [[] for i in range(81)]
        self.given_elements = self.grid != 0


    def solve(self):
        # Get rid of all future guesses and all future tried elements lists
        self.wipe_future(self.spots_solved)
        print(self.spots_solved)
        print(self.print_grid())
        row_index = self.get_row_index(self.spots_solved)
        col_index = self.get_col_index(self.spots_solved)

        # Exit condition
        if self.spots_solved == 81:
            return self.grid

        # If a cell doesn't have a solution in it, try to get one.
        elif not self.given_elements[row_index, col_index]:
            cell_candidates = self.get_cell_candidates(row_index,
                                                       col_index,
                                                       self.tried_elements)
            if len(cell_candidates) == 0:
                while True:
                    # TODO: potentially set element to 0 in here
                    row_index = self.get_row_index(self.spots_solved)
                    col_index = self.get_col_index(self.spots_solved)
                    if self.given_elements[row_index, col_index]:
                        self.spots_solved -= 1
                    else:
                        self.solve()
            # Aka, if there are possibilities for the cell:
            else:
                new_element = int(np.random.choice(cell_candidates,1))
                self.grid[row_index,col_index] = new_element
                self.spots_solved += 1
                self.tried_elements[self.spots_solved - 1].append(new_element)
                self.solve()


        # If a cell is already solved, move on
        else:
            self.spots_solved += 1
            self.solve()


    def get_row_index(self, spots_solved):
        return spots_solved // 9 


    def get_col_index(self, spots_solved):
        return spots_solved % 9


    # Once I've gone down a branch that doesn't pan out, I want to remove all 
    # future information that I've tried (future invalids and future guesses
    def wipe_future(self, spots_solved):
        for i in range(self.spots_solved, 81):
            row_index = self.get_row_index(i)
            col_index = self.get_col_index(i)
            self.tried_elements[i] = []
            if not self.given_elements[row_index, col_index]:
                self.grid[row_index, col_index] = 0


    # Get all of the possible values that a cell can take
    # If we've already tried 
    def get_cell_candidates(self, row_index, col_index, tried_elements):
        candidates = np.arange(1,10)
        for candidate in candidates:
            if not self.check_all(row_index, col_index, candidate) or\
            candidate in tried_elements:
                # Array version of list.remove():
                candidates = np.delete(candidates, 
                                       np.where(candidates == candidate))
        return candidates



solv = SudokuSolver(missing_3)
solv.solve()



