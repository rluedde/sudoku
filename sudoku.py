# Big-picture ideas for this: 
#   -An algo that solves a puzzle that you put in
#   -An algo that creates solvable puzzles
#       -aka generates a grid
#   -some graphics to make this playable by a user
#   -Option to choose between 9 unique letters or 9 unique numbers
#       -Maybe figure out how to use ASCII emojis lol
#   -Incorporate a database?
#       -What games the algo can solve the fastest?
#       -If I do a UI, store the order of the user's moves?
#   -Use OOP to represent the game

import numpy as np

class Sudoku:


    def __init__(self):
        self.grid = np.full((9,9), 0)

    # Have to be careful to not edit self.grid at all (i.e don't 
    # insert any "|")
    def print_grid(self):
        row_sep = "-------------"
        for i in range(9):
            # convert each line from an array of ints to a string
            # thru list comprehension(s) 
            line = "".join([str(element) for element in self.grid[i]])
            elements_passed = 0
            if i % 3 == 0:
                print(row_sep)
            line = f"|{line[0:3]}|{line[3:6]}|{line[6:9]}|"
            print(line)
        print(row_sep) # Print last set of dashes


    # Change element at row, col to guess
    def make_guess(self, row, col, guess):
        # Possible reindex row and col to make more sense
        # to a user...
        rg = range(0,9)
        g_rg = range(1,10)
        if row not in rg or col not in rg or guess not in g_rg:
            raise Exception ("Row, col, or guess out of range")
        self.grid[row, col] = guess
        return self.grid

    
    # Makes sure that a column contains only unique characters
    # Returns True if the column is all unique, False otherwise
    def col_clear(self, col_index):
        uniques = np.unique(self.grid[:,col_index])
        if len(uniques) == 9:
            return True
        else:
            return False 


    # Makes sure that a row contains only unique characters
    # Returns True is the row is all unique, False otherwise
    def row_clear(self, row_index):
        uniques = np.unique(self.grid[row_index, :])
        if len(uniques) == 9:
            return True
        else:
            return False

    # Iteratively calls col_clear and row_clear on all 9 cols to 
    # make sure they each only contain unique values. 
    # True if all rows and columns contain uniques, False otherwise
    # Rows and cols params signify how many rows and columns to 
    # check - used when checking quadrants
    def rows_cols_clear(self, rowcols_to_check = 9):
        for i in range(rowscols_to_check):
            if not self.row_clear(i) or not self.col_clear(i): 
                print(i)
                return False
        return True


    # Check if a quadrant contains only uniques
    # Returns True if the quadrant is all unique, False otherwise
    def quadrant_clear(self, beg_row, beg_col):
        uniques = np.unique(self.grid[beg_row:beg_row+3, beg_col:beg_col+3])
        if len(uniques) == 9:
            return True
        else:
            return False


    # Iteratively calls row_clear on all 9 rows to make sure they
    # each only contain unique values. 
    # True if all quadrants contain uniques, False otherwise
    # There's a better way to do this that doesn't require making
    # a new array quad_board
    # Also can probably combine this method with rows_cols_clear()
    def all_quadrants_clear(self):
        # Resize the board to be 3 * 27 for easier iteration.
        # Be careful of np.resize(arr) vs arr.resize()
        for i in range(9):
            beg_col = i % 3
            beg_row = i - (3 * beg_col)
            if not self.quadrant_clear(beg_row, beg_col):
                return False
        return True


    def all_clear():
        pass

