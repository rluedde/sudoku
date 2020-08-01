import {getInputArray, getGivenBoolArray, eraseCell} from "./ui.js"
import {setupGrid, drawCell} from "./setup_grid.js"
import {gameOver} from "./sudoku.js"
import {getGridString, getGrid} from "./save_game.js"
import {solver} from "./solver.js"

// TODO: for some reasonn .slice() and [...grid] don't work here for making
// copies. I tested both of these things in node and they worked fine...
// this function works tho
function copyGrid(grid) {
    // get the gridstring and then turn that string back into an array....
    let gridString = getGridString(grid)
    let gridCopy = getGrid(gridString)
    return gridCopy
}

// paint neccessary gridlines and current grid values
let grid = setupGrid()
// the copy is for the solving algorithm to use
let gridCopy = copyGrid(grid)

const givenBoolArray = getGivenBoolArray(grid)
const guessButton = document.getElementById("make_guess")
const saveButton = document.getElementById("save_game")
const loadButton = document.getElementById("load_game")
const solveButton = document.getElementById("solve")

// whenever the "Make Guess" button is clicked, make sure that the 
// guess's target is not a given location. put the guess there.
guessButton.onclick = function updateGrid() {
    let i, j, value
    [i, j, value] = getInputArray() 
    if (!givenBoolArray[i][j]) {
        eraseCell(i, j)
        grid = drawCell(i, j, parseInt(value), false, grid)
        if (gameOver(grid)) {
            alert("You won! Good work.")
            grid = setupGrid() 
            gridCopy = grid.slice()
        }
    }
    else {
        alert("You can't guess there!")
    }
}

saveButton.onclick = function saveGame() {
    let gridString = getGridString(grid)
    alert("Copy this string and save it for future use: \n\n" + gridString)

} 

loadButton.onclick = function readGridString() {
    const gridString = prompt("Please enter a string of digits output by a previous game!")
    grid = setupGrid(gridString)
}


solveButton.onclick = function(){solver(gridCopy)} 
