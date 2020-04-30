# Big-picture ideas for this: 
#   -An algo that solves a puzzle that you put in
#   -An algo that creates solvable puzzles
#       -aka generates a grid
#   -Two new classes: SudokuGenerator and SudokuSolver
#   -I'd get to practice with inheritance
#   -some graphics to make this playable by a user
#   -Option to choose between 9 unique letters or 9 unique numbers
#       -Maybe figure out how to use ASCII emojis lol
#   -Incorporate a database?
#       -What games the algo can solve the fastest?
#       -If I do a UI, store the order of the user's moves?
#   -Store games on disc somehow so you can come back to an old game!!

import numpy as np

class Sudoku:


    def __init__(self):
        # have a difficulty here?
        # for generation just do self.grid = SudokuGenerator.grid
        self.grid = np.full((9,9), 0)
        self.grid = np.array([[0,3,2,5,6,7,9,4,8],
                              [5,4,6,3,8,9,2,1,7],
                              [9,7,8,2,4,1,6,3,5],
                              [2,0,4,9,1,8,7,5,3],
                              [7,1,5,6,3,2,8,9,4],
                              [3,8,9,4,7,5,1,2,6],
                              [8,5,7,1,2,3,4,6,9],
                              [6,9,1,7,5,4,3,8,2],
                              [4,2,3,8,9,6,5,7,0]])

        self.answers = np.count_nonzero(self.grid)

    # Have to be careful to not edit self.grid at all (i.e don't 
    # insert any "|")
    def print_grid(self):
        col_guide = "  123 456 789"
        row_sep = " -------------"
        print(col_guide)
        for i in range(9):
            # convert each line from an array of ints to a string
            # thru list comprehension(s) 
            line =  "".join([str(element) for element in self.grid[i]])
            elements_passed = 0
            if i % 3 == 0:
                print(row_sep)
            line = str(i + 1) + f"|{line[0:3]}|{line[3:6]}|{line[6:9]}|"
            print(line)
        print(row_sep) # Print last set of dashes

    
    # Make sure that row, col and answer are all legal
    # Guesses are intuitive, a answer of 4 corresponds to the 
    # 4th row not the 5th. You make a play at a 0th row.
    def make_answer(self, row, col, answer):
        rg = range(1,10)
        if row not in rg or col not in rg or answer not in rg:
            print("Row, col, or answer out of range")
            return self.grid        

        index_row = row - 1 
        index_col = col - 1
        if self.grid[index_row, index_col] != 0:
            print("There is already a number there. Go again")
            return self.grid

        # If the inputs are valid and the target location is available,
        # check to see if the row, col or quad already have answer.
        # We return here for the unit tests - we wouldn't really need a 
        return self.check_answer(index_row, index_col, answer)

    
    # Make sure that the answer is legal, if it's not, return the previous 
    # version of the grid
    def check_answer(self, index_row, index_col, answer):

        if self.check_row(index_row, answer) and self.check_col(index_col, answer) and\
        self.check_quad(index_row, index_col, answer):
            self.grid[index_row,index_col] = answer
            return self.grid
        else:
            print("That number cannot go there")
            return self.grid


    # These check_XXX functions are for checking and making sure that 
    # a answer is legal. The XXX_clear functions are simply for the end
    # condition. 


    # Make sure answer isn't in row
    def check_row(self, row_index, answer):
        if answer in self.grid[row_index, :]:
            return False
        return True


    # Make sure answer isn't in col
    def check_col(self, col_index, answer):
        if answer in self.grid[:, col_index]:
            return False
        return True


    # Get the multiple of 3 that starts the quadrant of any index (row or col)
    def get_beg_index(self, index):
        return (index // 3) * 3


    # Make sure answer isn't in quadrant 
    def check_quad(self, row_index, col_index, answer):
        beg_row = self.get_beg_index(row_index)
        beg_col = self.get_beg_index(col_index)
 
        if answer in self.grid[beg_row:beg_row + 3, beg_col:beg_col + 3]:
            return False
        return True


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
    # check - might be useless 
    # Eventually return what row/col is a problem if there is one
    def rows_cols_clear(self, rowscols_to_check = 9):
        for i in range(rowscols_to_check):
            if not self.row_clear(i) or not self.col_clear(i): 
                return False
        return True


    # Check if a quadrant contains only uniques
    # Returns True if the quadrant is all unique, False otherwise
    def quadrant_clear(self, beg_row, beg_col):
        quadrant = self.grid[beg_row:beg_row+3, beg_col:beg_col+3]
        uniques = np.unique(quadrant)
        if len(uniques) == 9:
            return True
        else:
            return False


    # Iteratively call quadrant_clear on all 9 quads
    # Can probably combine this method with rows_cols_clear()
    # Eventually return what quadrant was issue
    def all_quadrants_clear(self):
        for beg_col in range(0,9,3):
            for beg_row in range(0,9,3):
                if not self.quadrant_clear(beg_row, beg_col):
                    return False
        return True


    # Call rows_cols_clear() and all_quadrants_clear() to make sure whole
    # board is valid
    def all_clear(self):
        if self.all_quadrants_clear() and self.rows_cols_clear():
            return True
        return False


    def game_over(self):
        # If 0 not in grid and all quadrants clear and rowscols clear
        # then return True
        if (0 not in self.grid) & self.all_clear():
            return True
        return False


