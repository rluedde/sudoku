import numpy as np
from sudoku import Sudoku
from time import sleep
import sys
sys.setrecursionlimit(2500)

missing_3 = np.array([[0,3,2,5,6,0,0,4,8],
                      [5,4,6,0,8,0,2,0,7],
                      [9,7,0,2,0,0,0,3,5],
                      [2,0,4,9,1,0,7,0,0],
                      [0,0,0,6,3,2,0,9,4],
                      [3,8,9,0,0,5,0,2,6],
                      [8,5,7,0,2,3,0,6,9],
                      [6,9,1,0,5,0,0,8,2],
                      [4,2,3,0,0,0,5,7,0]])

hard_ones = np.array([[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,3,0,8,5],
                      [0,0,1,0,2,0,0,0,0],
                      [0,0,0,5,0,7,0,0,0],
                      [0,0,4,0,0,0,1,0,0],
                      [0,9,0,0,0,0,0,0,0],
                      [5,0,0,0,0,0,0,7,3],
                      [0,0,2,0,1,0,0,0,0],
                      [0,0,0,0,4,0,0,0,9]])

class SudokuSolver(Sudoku):


    def __init__(self, grid):
        self.grid = grid
        self.spots_solved = 0
        self.tried_elements = [[] for i in range(81)]
        self.given_elements = self.grid != 0


    def solve(self):
        # Get rid of all future guesses and all future tried elements lists
        self.wipe_future(self.spots_solved)
        print("\n", self.spots_solved, "\n")
        self.print_grid()
        row_index = self.get_row_index(self.spots_solved)
        col_index = self.get_col_index(self.spots_solved)

        # Exit condition
        if self.spots_solved == 81:
            return self.grid
        else: # find a solution or backtrack
            candidates = self.get_cell_candidates(row_index,
                                                  col_index)
            # sleep(.5)
            # if spot's given, move on
            if self.given_elements[row_index,col_index]:
                self.spots_solved += 1
                self.solve()

            # if the cell isn't given and has no solutions, backtrack 
            elif not self.given_elements[row_index, col_index] and\
            len(candidates) == 0:
                print("hi", candidates)
                # go back to closest cell that's not given
                while True:
                    self.spots_solved -= 1
                    row_index = self.get_row_index(self.spots_solved)
                    col_index = self.get_col_index(self.spots_solved)
                    if not self.given_elements[row_index, col_index]:
                        break
                self.wipe_future(self.spots_solved)
                # self.grid[row_index,col_index] = 0
                # TODO: clear all future tries
                self.solve()
            
            # if there's solutions, pick one randomly, record that we've
            # tried it
            else:
                print(candidates)
                new_element = int(np.random.choice(candidates,1))
                self.grid[row_index,col_index] = new_element
                self.spots_solved += 1
                self.tried_elements[self.spots_solved - 1].append(new_element)
                self.solve()



    """
        # If a cell doesn't have a solution in it, try to get one.
        elif not self.given_elements[row_index, col_index]:
            candidates = self.get_cell_candidates(row_index,
                                                  col_index)
            sleep(.5)

            print("candies: ", candidates)
            while len(candidates) == 0:
                # Get back to a non-given position where there are
                # possibilities
                # TODO: potentially set element to 0 in here

                row_index = self.get_row_index(self.spots_solved)
                col_index = self.get_col_index(self.spots_solved)
                candidates = self.get_cell_candidates(row_index,
                                                      col_index)

                # if it's a given cell (True): go back a cell
                # elif it's a nongiven cell (False): try a guess that hasn't
                # been tried yet
                if self.given_elements[row_index, col_index] or\
                len(candidates == 0):
                    print("carti!")
                    self.spots_solved -= 1
                elif not self.given_elements[row_index,col_index] and\
                len(candidates) != 0:
                    self.solve()
                # else: just keep decrementing
                    

            # Aka, if there are possibilities for the cell:
            else:
                new_element = int(np.random.choice(candidates,1))
                self.grid[row_index,col_index] = new_element
                self.spots_solved += 1
                self.tried_elements[self.spots_solved - 1].append(new_element)
                self.solve()


        # If a cell is already solved, move on
        else:
            self.spots_solved += 1
            self.solve()
    """

    def get_row_index(self, spots_solved):
        return spots_solved // 9 


    def get_col_index(self, spots_solved):
        return spots_solved % 9


    # Once I've gone down a branch that doesn't pan out, I want to remove all 
    # future information that I've tried (future invalids and future guesses
    # It might have to be the spot AFTER the current one, we don't want
    # to remove the current cell's trieds but we do want to remove it's
    # actual guess
    # TODO: make sure the above shit happens
    def wipe_future(self, spots_solved):
        for i in range(self.spots_solved + 1, 81):
            row_index = self.get_row_index(i)
            col_index = self.get_col_index(i)
            self.tried_elements[i] = []
            if not self.given_elements[row_index, col_index]:
                self.grid[row_index, col_index] = 0


    # Get all of the possible values that a cell can take
    # TODO: if we've tried a value, it's not a candidate
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



solv = SudokuSolver(hard_ones)
solv.solve()



