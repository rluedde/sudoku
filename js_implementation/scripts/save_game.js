export function getGridString(grid) {
    const singleArray = grid.reduce(function(accum, arr) {
        accum.push(...arr)
        return accum
    }) 
    const gridString = singleArray.reduce((accum, num) => accum + String(num))
    return gridString
}

export function getGrid(gridstring) {
    const gridArr = gridstring.split("").map(element => parseInt(element))
    const grid = []
    gridArr.forEach(function(_, index){
        if (index % 9 === 0) {
            grid.push(gridArr.slice(index, index + 9))
        }
    })
    return grid
}