var c = document.getElementById("canvas");
var ctx = c.getContext("2d");
var grid = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,3,0,0,0,0],
            [9,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0]]
const width = 70


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

function drawCell(i, j, value, given) {
    //row
    this.i = i;
    //col
    this.j = j;
    this.given = given;
    this.value = value;
    // ctx.beginPath()
    if (given) {
        ctx.font = "40px Apercu Mono"
    }
    else {
        ctx.font = "50px Apercu Mono"
    }

    ctx.strokeText(String(value), j * width + 23, i * width + 52)
    ctx.stroke()

    
    // if given, draw number bolded
    // else, draw shit normal

}

// go through the var grid and create a cell object in grid
// 0's don't get put on the canvas
function populateGrid() {
    for(var i = 0; i < 9; i++){
        for(var j = 0; j < 9; j++) {
            const grid_value = grid[i][j]
            console.log(i,j)
            given = true  
            drawCell(i, j, grid_value, given)
        }
    }

}


drawGridLines()
populateGrid()
// while the game isn't over, get guesses and make those guesses
// non-bold (no idea how to get guesses here)







