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


// should use bool array to determine
function eraseNumber(i, j) {
    pass
}

const guess_button = document.getElementById("make_guess")

guess_button.onclick = function updateGrid() {
    const input = getInputArray()
    drawCell(...input, false)
}

const erase_button = document.getElementById("erase_guess")

erase_button.onclick = function eraseCell() {
    // use bool array to not erase givens
    let i, j, dummy
    [i, j, dummy] = getInputArray();
    console.log(i, j)
    i++
    j++
    ctx.clearRect(j * 70 - 62, i * 70 - 65, 55, 55)
}