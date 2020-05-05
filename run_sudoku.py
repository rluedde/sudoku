from sudoku import Sudoku
from sudoku_generator import SudokuGenerator

class InputError(BaseException):
    pass

def main():
    game = Sudoku() # Start a game
    print("Please wait, the grid is being generated")
    genned_grid = SudokuGenerator().generate()
    game.grid = genned_grid 
    print_instructions()
    first_guess = True
    while game.game_over() == False:
        # Show user the grid if it's their first guess
        if first_guess:
            print("Here's the grid:\n")
            game.print_grid()
            first_guess = False
        try: 
            play = input("\nGive your answer (r,c,a): ")
            if play.strip() == "q":
                return "Have a good day!"
            row, col, answer = (int(num) for num in play.split(","))
            # If the user enters a guess in the right format
            # but the bounds on one of the guess elements are wrong, 
            # the board gets printed even though there's no change.
            # Only print the board when there's a change....
            game.make_answer(row,col,answer)
            game.print_grid()
        except ValueError:
            print("Please enter the answer in the right format!")
        except InputError:
            print("Row, col, and answer must be 1-9")
    return "Victory!"
        

def print_instructions():
    print("\nWelcome to Sudoku!")
    print("Guess \"q\" to quit!")
    print("An answer is structured like this: row, col, answer")
    print("Ex. 8,8,9 - no spaces!\n")


if __name__ == "__main__":
    print(main())
