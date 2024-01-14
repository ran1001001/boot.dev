const { crawlPage, getURLsFromHTML } = require('./crawl.js')

//an array, the third element is the first argument from command line
const clArgs = process.argv

//if third element is present call main() with that element as input, otherwise console error
clArgs.length === 3 ? main(clArgs[2]) : console.error("Error: no url or multiple urls provided.");

async function main(baseUrl) {
    console.log(`Crawl starting in "${baseUrl}"...`)
    const htmlString = await crawlPage(baseUrl)
    console.log(getURLsFromHTML(htmlString, baseUrl))
}

