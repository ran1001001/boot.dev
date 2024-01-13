const { crawlPage } = require('./crawl.js')

//an array, the third element is the first argument from command line
const clArgs = process.argv

//if third element is present call main() with that element as input, otherwise console error
clArgs.length === 3 ? main(clArgs[2]) : console.error("Error: no url or multiple urls provided.");

function main(baseUrl) {
    console.log(`Crawling starting in "${baseUrl}"...`)
    crawlPage(baseUrl)
}

