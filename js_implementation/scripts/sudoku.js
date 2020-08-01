/*

// determine if the game is over given a grid
export function gameOver(grid) {
    for (var i = 0; i < grid.length; i++) {
        if (!checkForZeros(grid[i]) ||
            !checkRow(grid[i]) ||
            !checkCol(grid, i) ||
            !checkQuad(grid, i)) {
                return false
            } 
    }
    return true
}

export function boardValid(grid) {
    // essentially, I need to change allUnique to make sure that the only
    // repeated digits are zeros. I can do this by filtering out all zeros from a 
    // row/col/quad
    for (var i = 0; i < grid.length; i++) {
        if (!checkRow(grid[i], over = false) ||
            !checkCol(grid, i, over = false) ||
            !checkQuad(grid, i, over = false)) {
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
function checkRow(row, over) {
    return allUnique(row, over)
}

function checkCol(grid, col_index, over) {
    var col = []
    // iterate through each row and grab the each column value at for a 
    // specific column (col_index)
    for (var i = 0; i < 9; i++) {
        const col_val = grid[i][col_index]
        col.push(col_val)
    } 
    return allUnique(col, over)
}

function checkQuad(grid, index, over) {
    const beg_row = Math.floor(index/3) * 3
    const beg_col = (index % 3) * 3
    // construct array with eleemnts from index-th quadrant
    var quad = []
    for (var i = 0; i < 3; i++) {
        row = grid[beg_row + i]
        const quad_piece = row.slice(beg_col, beg_col + 3)
        quad.push(...quad_piece)
    }
    return allUnique(quad, over)
}
*/
// callback function that returns if the index of a value of 
// an array is equal to the index. It will return false if there
// are duplicated values in the index
function uniqueNonZeros(value, index, self) {
    return (self.indexOf(value) === index && value !== 0) ;
}

function nonZeros(value) {
    return (value !== 0)
}

function allUnique(array, over = false) {
    const uNZ = array.filter(uniqueNonZeros)
    if (over) {
        return (uNZ.length === 9)
    }
    else {
        const NZ = array.filter(nonZeros)
        return (JSON.stringify(uNZ) === JSON.stringify(NZ))
    }

}

var test_arr = [1,2,3,4,5,0,7,6,8]
var unique = allUnique(test_arr, over = false)

console.log(unique)