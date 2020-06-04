import {getInputArray, eraseCell, getGivenBoolArray} from "./ui.js"
import {newGrid, drawBackGround, drawGridLines, populateGrid, drawCell} from "./setup_grid.js"
import {gameOver} from "./sudoku.js"


var grid = newGrid()
drawBackGround()
drawGridLines()
populateGrid(grid)

const givenBoolArray = getGivenBoolArray(grid)
const guess_button = document.getElementById("make_guess")
guess_button.onclick = function updateGrid() {
    let i, j, value
    [i, j, value] = getInputArray() 
    if (!givenBoolArray[i][j]) {
        eraseCell(i, j)
        grid = drawCell(i, j, parseInt(value), false, grid)
        if (gameOver(grid)) {
            alert("You won! Good work.")
            grid = newGrid()
            //TODO: get a new board. i think just have a function that returns 
            // a board so we'd go a grid = newGrid() right here
            drawBackGround()
            drawGridLines()
            populateGrid(grid)
        }
        console.log(grid)
    }
    else {
        alert("You can't guess there!")
    }
}