var c = document.getElementById("canvas");
export var ctx = c.getContext("2d");
export var grid =  [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,3,0,0,0,0,0,0],
                    [0,0,0,0,0,0,9,0,0],
                    [0,0,0,0,3,0,0,4,0],
                    [9,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,1],
                    [0,0,0,0,1,0,0,0,0]]
const width = 70

//draw background - neccessary for erasing
function drawBackGround() {
    ctx.beginPath();
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, c.width, c.height);
}

function drawGridLines() {
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

export function drawCell(i, j, value, given) {
    if (value !== 0) {
        if (given) {
            ctx.font = "100 50px Arial"
        }
        else {
            ctx.font = "900 50px Arial"
        }
        ctx.strokeText(String(value), j * width + 21, i * width + 52)
        ctx.stroke()
    }

}

// go through the var grid and create a cell object in grid
// 0's don't get put on the canvas
function populateGrid() {
    for(var i = 0; i < 9; i++){
        for(var j = 0; j < 9; j++) {
            const grid_value = grid[i][j]
            const given = true  
            drawCell(i, j, grid_value, given)
        }
    }

}

drawBackGround()
drawGridLines()
populateGrid()
// updateGrid()
// while the game isn't over, get guesses and make those guesses
// non-bold (no idea how to get guesses here)







