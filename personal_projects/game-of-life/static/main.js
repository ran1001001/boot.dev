function startDrawing() {
    isDrawing = true;
    draw.call(this); // Draw the initial cell immediately, passing the current div/cell
}

function draw() {
    if (isDrawing) {
        this.classList.toggle("active");
    }
}

function stopDrawing() {
    isDrawing = false;
}

function evolveGrid(gridSize, currentGrid) {
    const numRows = gridSize;
    const numCols = gridSize;

    const nextGeneration = currentGrid.slice(); // Create a copy of the current grid

    // Function to get the index in the 1D array from 2D coordinates with modulo
    const getIndex = (row, col) => ((row + numRows) % numRows) * numCols + ((col + numCols) % numCols);

    for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            const cellIndex = getIndex(row, col);
            let liveNeighbors = 0;

            // Iterate over neighboring cells using modulo
            for (let i = -1; i <= 1; i++) {
                for (let j = -1; j <= 1; j++) {
                    if (i === 0 && j === 0) continue; // Skip the central cell
                    const neighborIndex = getIndex(row + i, col + j);
                    liveNeighbors += currentGrid[neighborIndex];
                }
            }

            // Apply Conway's Game of Life rules
            if (currentGrid[cellIndex] === 1) {
                nextGeneration[cellIndex] = liveNeighbors === 2 || liveNeighbors === 3 ? 1 : 0;
            } else {
                nextGeneration[cellIndex] = liveNeighbors === 3 ? 1 : 0;
            }
        }
    }

    return nextGeneration;
}

function play(gridSize) {
    //initialize current grid's cells states
    const currentGrid = []
    for (let i = 0; i < divs.length; i++) {
        const div = divs[i];
        if (div.classList[1]) {
            currentGrid.push(1)
        } else {
            currentGrid.push(0)
        }
    }

    //apply game logic for next generation
    const nextGrid = evolveGrid(gridSize, currentGrid)

    //render next generation's grid state
    for (let i = 0; i < divs.length; i++) {
        const div = divs[i];
        const cellState = nextGrid[i]
        if (cellState === 0) {
            div.classList.remove("active")
        } else {
            div.classList.add("active")
        }
    }
}

function createCells(size, container) {
    const sizeGrid = size * size
    for (let i = 0; i < sizeGrid; i++) {
        const div = document.createElement('div')
        div.classList.add('cell')
        container.appendChild(div)
    }
    return document.querySelectorAll('.cell')
}

function setupCells(divs) {
    divs.forEach(element => {
        element.addEventListener("mousedown", startDrawing);
        element.addEventListener("mouseenter", draw);
        element.addEventListener("mouseup", stopDrawing);
    });
}

//initialize divs
let divs;
//get size from div #size-result
let sizeResult = document.getElementById('size-result')
let size = +sizeResult.innerText.slice(0, 2)
//handle drawing on grid
let isDrawing = false;
//play/stop control on interval and toggle "running" state
let playInterval;
let clicked = false;
const gridState = document.getElementById("grid-state")
const playButton = document.getElementById("play-button")
const stopButton = document.getElementById("stop-button")
playButton.addEventListener("click", () => {
    if (!clicked) {
        playInterval = setInterval(function() {play(size)}, 130)
        clicked = true
        gridState.innerText = "Game Playing..."
    }
})
stopButton.addEventListener("click", () => {
    clicked = false
    clearInterval(playInterval)
    gridState.innerText = "Game Not Playing"
})

//create and setup cells
const container = document.getElementById('grid-container')
//create cells as divs
divs = createCells(size, container)
//add event listeners for each divs to draw on grid
setupCells(divs)
//style the grid
container.style.gridTemplateColumns = `repeat(${size}, 20px)`
