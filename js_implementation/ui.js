import {drawCell, grid, ctx} from "./setup_grid.js"


function getInputArray() {
    const row = document.getElementById('row').value;
    const col = document.getElementById('col').value;
    const value = document.getElementById('value').value;
    return [row - 1, col - 1, value];
}


function getGivenBoolArray(grid) {
    const boolArr = []
    for (var i = 0; i < grid.length; i++) {
        row = grid[i]
        const bool_row = row.map(val => val === 0 ? false : true)
        boolArr.push(bool_row)
    }
    return boolArr
}


function eraseCell(i, j) {
    // use bool array to not erase givens
    console.log(i, j)
    i++
    j++
    ctx.clearRect(j * 70 - 62, i * 70 - 65, 55, 55)
}

const guess_button = document.getElementById("make_guess")

guess_button.onclick = function updateGrid() {
    let i, j, value
    [i, j, value] = getInputArray() 
    let givenBoolArray = getGivenBoolArray(grid)
    if (givenBoolArray[i][j]) {
        alert("You can't guess there!")
    }
    else {
        eraseCell(i, j)
        drawCell(i, j, value, false)
    }
}
