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


    def print_grid(self):
        row_sep = "-------------"
        for i in range(9):
            line = self.grid[i] 
            elements_passed = 0
            if i % 3 == 0:
                print(row_sep)
            for z in range(13): 
                if elements_passed == 3 or z == 0:
                    line.insert(z, "|")
                    elements_passed = 0
                else:
                    elements_passed += 1
            print("".join(line))
        print(row_sep)



game = Sudoku()
game.print_grid()
