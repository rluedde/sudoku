from sudoku import Sudoku

class InputError(BaseException):
    pass

def main():
    g = Sudoku()    
    print_instructions()
    first_guess = True
    while g.game_over() == False:
        # Show user the grid if it's their first guess
        if first_guess:
            print("Here's the grid:\n")
            g.print_grid()
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
            g.make_answer(row,col,answer)
            g.print_grid()
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
