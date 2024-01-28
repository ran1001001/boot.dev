const { readFile } = require('fs').promises
const express = require('express')
const app = express()

app.use(express.static('static'))
app.get('/', async (req, res) => {
    const html = await readFile('./static/game.html', 'utf-8')
    res.send(html)
})

app.listen(3000, () => {
    console.log("we're cooking...")
})
