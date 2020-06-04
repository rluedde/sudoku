// determine if the game is over given a grid
export function gameOver(grid) {
    for (var i = 0; i < grid.length; i++) {
        if (!checkForZeros(grid[i]) ||
            !checkRow(grid[i]) ||
            !checkCol(grid, i) ||
            !checkQuad(i)) {
                return false
            } 
    }
    return true
}
    

// check if there's any zeros on the board 
function checkForZeros(row) {
    return (!row.includes(0))
}


// the next three functions make sure that each row, col, and quadrant
// contains 9 unique values
function checkRow(row) {
    return allUnique(row)
}

function checkCol(grid, col_index) {
    var col = []
    // iterate through each row and grab the each column value at for a 
    // specific column (col_index)
    for (var i = 0; i < 9; i++) {
        const col_val = grid[i][col_index]
        col.push(col_val)
    } 
    return allUnique(col)
}

function checkQuad(index) {
    return true
}


// callback function that returns if the index of a value of 
// an array is equal to the index. It will return false if there
// are duplicated values in the index
function unique(value, index, self) {
    return self.indexOf(value) === index;
}

function allUnique(array) {
    array = array.filter(unique)
    /*
    if (array.length === 9) {
        return true
    }
    return false
    */
   return (array.length === 9)

}