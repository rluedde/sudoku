import {getGrid} from "./access_token.js"

var c = document.getElementById("canvas");
export var ctx = c.getContext("2d");
const width = 70

export function newGrid() {
    //TODO: call a generation algorithm or something to 
    // generate a new board here. 
    return  [[0,5,6,2,1,4,7,3,9],
             [1,9,3,5,7,6,8,4,2],
             [2,4,7,9,8,3,1,6,5],
             [4,6,2,7,5,9,3,8,1],
             [9,3,1,8,6,2,4,5,7],
             [7,8,5,3,4,1,9,2,6],
             [6,2,4,1,9,8,5,7,3],
             [3,7,9,4,2,5,6,1,8],
             [5,1,8,6,3,7,2,9,4]]
}


//draw background - neccessary for erasing
export function drawBackGround() {
    ctx.beginPath();
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, c.width, c.height);
}

export function drawGridLines() {
    for(var i = 0; i < 10; i++) {
        if (i % 3 === 0) {
            ctx.lineWidth = 5;
        }
        else {
            ctx.lineWidth = 2;
        }
        ctx.beginPath()

        // draw horiz lines
        ctx.moveTo(0,i * width);
        ctx.lineTo(630, i * width);
        // draw vert lines
        
        ctx.moveTo(i * width, 0);
        ctx.lineTo(i * width, 630)

        ctx.stroke();
    }
}

export function drawCell(i, j, value, given, grid) {
    if (value !== 0) {
        if (given) {
            ctx.font = "100 50px Arial"
        }
        else {
            ctx.font = "900 50px Arial"
            grid[i][j] = value
        }
        ctx.strokeText(String(value), j * width + 21, i * width + 52)
        ctx.stroke()
    }
    return grid

}

// go through the var grid and create a cell object in grid
// 0's don't get put on the canvas
export function populateGrid(grid) {
    for(var i = 0; i < 9; i++){
        for(var j = 0; j < 9; j++) {
            const grid_value = grid[i][j]
            const given = true  
            drawCell(i, j, grid_value, given)
        }
    }

}

export function setupGrid(givenGrid = -1) {
    let grid
    // in the case that the user doesn't specify a gridString,
    // just build them their own - eventually newGrid() will 
    // contain a backtracking generation algorithm
    if (givenGrid === -1) {
        grid = newGrid()

    } else {
        // in the case that the user comes prepared with their own gridString
        grid = getGrid(givenGrid)
    }
    drawBackGround()
    drawGridLines()
    populateGrid(grid)
    return grid
}


// while the game isn't over, get guesses and make those guesses
// non-bold (no idea how to get guesses here)







