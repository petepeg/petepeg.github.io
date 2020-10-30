///////////////////////////
// Conway's Game of Life //
///////////////////////////
// Peter Pegues

let pause = true;
let gameBoardEmpty = Array(60).fill().map(() => Array(60).fill(0));
let gameBoard = JSON.parse(JSON.stringify(gameBoardEmpty)); // Deep clone
let gameBoardNext = JSON.parse(JSON.stringify(gameBoardEmpty));

let gameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 600;
        this.canvas.height = 600;
        this.canvas.id = "canvas";
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.frameNo = 0;
        this.interval = setInterval(updateGameArea, 100);
        this.canvas.addEventListener("mousedown", addRemCell, false);
        this.canvas.addEventListener("contextmenu", event => event.preventDefault());
    },
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

function getPos(event) {
    let x = event.x;
    let y = event.y;
    let canvas = document.getElementById("canvas");
    x -= canvas.offsetLeft;
    y -= canvas.offsetTop;
    ax = ~~(x/10); // divide by 10 discard decimal
    ay = ~~(y/10);
    return [ax,ay]
}

function addRemCell(event) {
    event.preventDefault();
     let pos = getPos(event);
     let x = pos[0];
     let y = pos[1];
     if(event.button == 0){
         gameBoard[y][x] = 1;
     }else if(event.button == 2){
        gameBoard[y][x] = 0;
     }
}

function playPause() {
    pause = pause ? false:true;
}

function lifeCheck() {
    for(let i = 0; i < 60; i++) {
        for(let j = 0; j < 60; j++) {
            let result = checkAdjacent(i,j);
            if(gameBoard[i][j] == 0) { // dead cell
                if(result == 3) {
                    gameBoardNext[i][j] = 1; // cell birth
                } else {
                    gameBoardNext[i][j] = 0; // continue to be dead
                }
            } else if (gameBoard[i][j] == 1) { // live cell
                if(result < 2 || result > 3) {
                    gameBoardNext[i][j] = 0; // dies
                } else {
                    gameBoardNext[i][j] = 1; // continue to live
                }
            } else {
                console.log(`Something went horribly wrong at ${i},${j}`)
            }
        }
    }
    gameBoard = JSON.parse(JSON.stringify(gameBoardNext)); // Deep clone
}

// Return number of live neighbors
function checkAdjacent(row,col) {
    let rowi = row - 1;
    let colj = col - 1;
    let result = 0;
    for(let i = 0; i < 3; i++) {
        if( i+rowi >= 0 && i+rowi < 60) {
            for(let j = 0; j < 3; j++) {
                if( j+colj >= 0 && j+colj < 60) {
                    // Don't look at yourself
                    if(rowi+i != row || colj+j != col){
                        let state = gameBoard[i+rowi][j+colj];
                        if(state > 0) {
                            result += 1;
                        }
                    }
                }
            }
        }
    }
    return result;
}

function clearBoard() {
    gameBoard = JSON.parse(JSON.stringify(gameBoardEmpty)); // Deep clone
    gameBoardNext = JSON.parse(JSON.stringify(gameBoardEmpty));
}

function gliderGun() {
    clearBoard();
    gameBoard[5][1] = 1;
    gameBoard[5][2] = 1;
    gameBoard[6][1] = 1;
    gameBoard[6][2] = 1;
    gameBoard[5][11] = 1;
    gameBoard[6][11] = 1;
    gameBoard[7][11] = 1;
    gameBoard[4][12] = 1;
    gameBoard[8][12] = 1;
    gameBoard[3][13] = 1;
    gameBoard[9][13] = 1;
    gameBoard[3][14] = 1;
    gameBoard[9][14] = 1;
    gameBoard[6][15] = 1;
    gameBoard[4][16] = 1;
    gameBoard[8][16] = 1;
    gameBoard[5][17] = 1;
    gameBoard[6][17] = 1;
    gameBoard[7][17] = 1;
    gameBoard[6][18] = 1;
    gameBoard[3][21] = 1;
    gameBoard[4][21] = 1;
    gameBoard[5][21] = 1;
    gameBoard[3][22] = 1;
    gameBoard[4][22] = 1;
    gameBoard[5][22] = 1;
    gameBoard[2][23] = 1;
    gameBoard[6][23] = 1;
    gameBoard[1][25] = 1;
    gameBoard[2][25] = 1;
    gameBoard[6][25] = 1;
    gameBoard[7][25] = 1;
    gameBoard[3][35] = 1;
    gameBoard[4][35] = 1;
    gameBoard[3][36] = 1;
    gameBoard[4][36] = 1;
}

function drawGrid() {
    ctx = gameArea.context;
    // Change color on pause
    if(pause == true) {
        ctx.fillStyle = "grey";    
    } else {
        ctx.fillStyle = "black";
    }
    //draw grid lines
    for(let i = 1; i <= 60; i++) {
        let h = 10 * i
        this.ctx.fillRect(0, h, 600, 1);
        this.ctx.fillRect(h, 0, 1, 600);
    }
    // draw cells
    for(let i = 0; i < 60; i++) {
        for(let j = 0; j < 60; j++) {
            if(gameBoard[i][j] == 1) {
                ctx.fillRect(j*10, i*10, 10, 10);
            }
        }
    }
}


function updateGameArea() {
    gameArea.clear();
    drawGrid();

    if(pause == false){
        lifeCheck();
    }

}
