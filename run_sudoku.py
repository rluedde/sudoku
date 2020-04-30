from sudoku import Sudoku

class InputError(BaseException):
    pass

def main():
    g = Sudoku()    
    print("\nWelcome to Sudoku!")
    print("Guess \"q\" to quit!")
    print("An answer is structured like this: row, col, answer")
    print("Ex. 8,8,9 - no spaces!\n")
    while g.game_over() == False:
    # for i in range():
        print("Here's the grid:\n")
        g.print_grid()
        try: 
            play = input("\nGive your answer (r,c,a): ")
            if play.strip() == "q":
                return "Have a good day!"
            row, col, answer = (int(num) for num in play.split(","))
            g.make_answer(row,col,answer)
        except ValueError:
            print("Please enter the answer in the right format!")
        except InputError:
            print("Row, col, and answer must be 1-9")
    return "Victory!"
        
if __name__ == "__main__":
    print(main())
