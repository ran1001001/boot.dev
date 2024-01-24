const divs = document.querySelectorAll('.cell')
divs.forEach(element => {
    element.addEventListener("click", active);
});

function active() {
  this.classList.add("active")
}

function evolveGrid(currentGrid) {
    const numRows = 12;
    const numCols = 12;

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

function play() {
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
    const nextGrid = evolveGrid(currentGrid)

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
