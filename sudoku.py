# Ideas for this: 
#    -An algo that solves a puzzle that you put in
#   -An algo that creates solvable puzzles
#   -some graphics to make this playable by a user
#   -Option to choose between 9 unique letters or 9 unique numbers
#       -Maybe figure out how to use ASCII emojis lol
#   -Incorporate a database?
#       -What games the algo can solve the fastest?
#       -If I do a UI, store the order of the user's moves?
#   -Use OOP to represent the grid?


class Sudoku:


    def __init__(self):
        self.grid = [["0", "0", "0", "0", "0", "0", "0", "0", "0"], 
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]



    # Have to be careful to not edit self.grid at all (i.e don't 
    # insert any "|")
    def print_grid(self):
        row_sep = "-------------"
        for i in range(9):
            line = "".join(self.grid[i])
            elements_passed = 0
            if i % 3 == 0:
                print(row_sep)
            line = f"|{line[0:3]}|{line[3:6]}|{line[6:9]}|"
            print(line)
        print(row_sep) # Print last set of dashes



    def make_guess(self, row, col, guess):
        # Reindex row and col so they make sense to user 
        row -= 1
        col -= 1
        self.grid[row][col] = guess




game = Sudoku()
game.print_grid()
game.make_guess(3, 1, "8")
game.print_grid()
