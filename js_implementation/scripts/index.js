import {getInputArray, eraseCell, getGivenBoolArray} from "./ui.js"
import {setupGrid, drawCell} from "./setup_grid.js"
import {gameOver} from "./sudoku.js"

// paint neccessary gridlines and current grid values
var grid = setupGrid()

const givenBoolArray = getGivenBoolArray(grid)
const guess_button = document.getElementById("make_guess")

// whenever the "Make Guess" button is clicked, make sure that the 
// guess's target is not a given location. put the guess there.
guess_button.onclick = function updateGrid() {
    let i, j, value
    [i, j, value] = getInputArray() 
    if (!givenBoolArray[i][j]) {
        eraseCell(i, j)
        grid = drawCell(i, j, parseInt(value), false, grid)
        // TODO: generate some sort of hash right here and use that as
        // part of the URL for a certain game
        if (gameOver(grid)) {
            alert("You won! Good work.")
            grid = setupGrid() 
        }
    }
    else {
        alert("You can't guess there!")
    }
}