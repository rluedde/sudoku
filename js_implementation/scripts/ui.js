import {ctx} from "./setup_grid.js"

export function getInputArray() {
    const row = document.getElementById('row').value;
    const col = document.getElementById('col').value;
    const value = document.getElementById('value').value;
    return [row - 1, col - 1, value];
}


export function getGivenBoolArray(grid) {
    const boolArr = []
    let row = []
    for (var i = 0; i < grid.length; i++) {
        row = grid[i]
        const bool_row = row.map(val => val === 0 ? false : true)
        boolArr.push(bool_row)
    }
    return boolArr
}

export function eraseCell(i, j) {
    i++
    j++
    ctx.clearRect(j * 70 - 62, i * 70 - 65, 55, 55)
}