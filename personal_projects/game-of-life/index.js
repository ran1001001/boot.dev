const { readFile } = require('fs').promises
const express = require('express')
const app = express()

app.get('/', async (req, res) => {
    const html = await readFile('./test.html', 'utf-8')
    res.send(html) 
})

app.listen(3000, () => {
    console.log("we're cooking...")
})
