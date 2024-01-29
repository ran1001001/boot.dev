const { readFile } = require('fs').promises
const express = require('express')
const app = express()

// serve static
app.use(express.static('static'))
//parse html forms url-encoded bodies
app.use(express.urlencoded({ extended: true }))
app.get('/', async (req, res) => {
    const html = await readFile('./static/index.html', 'utf-8')
    res.send(html)
})
app.post('/create', async (req, res) => {
    const size = req.body.size
    const html = `
    <div id="main-container">
        <button id="play-button">play</button>
        <button id="stop-button">stop</button>
        <div class="grid-container" id="grid-container"></div>
    </div>
    <script src="main.js">
        const container = document.getElementById('grid-container')
        divs = createCells(${size}, container)//customize size
        setupCells(divs)
        container.style.gridTemplateColumns = 'repeat(${size}, 20px)'
    </script>`
    res.send(html)
})

app.listen(3000, () => {
    console.log("we're cooking...")
    console.log("Go to: http://localhost:3000")
})
