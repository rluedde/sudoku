import {getInputArray, getGivenBoolArray} from "./ui.js"
import {setupGrid, drawCell, ctx} from "./setup_grid.js"
import {gameOver} from "./sudoku.js"

/*
// Start the main app logic.
requirejs(['ui', 'setup_grid', 'sudoku'],
function   ($,        canvas,   sub) {
    //jQuery, canvas and the app/sub module are all
    //loaded and can be used here now.
});
*/
// paint neccessary gridlines and current grid values
var grid = setupGrid()

const givenBoolArray = getGivenBoolArray(grid)
const guessButton = document.getElementById("make_guess")
const saveButton = document.getElementById("save_game")
const loadButton = document.getElementById("load_game")

function eraseCell(i, j) {
    i++
    j++
    ctx.clearRect(j * 70 - 62, i * 70 - 65, 55, 55)
}

// whenever the "Make Guess" button is clicked, make sure that the 
// guess's target is not a given location. put the guess there.
guessButton.onclick = function updateGrid() {
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