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
    <h1 id="size-result">${size} x ${size}</h1>
    <h2 id="grid-state">Game Not Playing</h2>
    <div class="controls-container">
        <button onclick="location.href='/'">Go back</button>
    </div>
    <div style="margin: 60px 0px 25px 0px" class="controls-container">
        <button id="play-button">play</button>
        <button id="stop-button">stop</button>
    </div>
    <div id="main-container">
        <div class="grid-container" id="grid-container"></div>
    </div>
    <script src="main.js" type="text/javascript"></script>`
    res.send(html)
})

app.listen(3000, () => {
    console.log("we're playing...")
    console.log("Go to: http://localhost:3000")
})
