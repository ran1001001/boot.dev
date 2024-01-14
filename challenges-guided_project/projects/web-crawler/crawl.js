const { JSDOM } = require('jsdom')

function normalizeURL(urlStr) {
    let url = require('node:url').parse(urlStr);
    let hostname = url.hostname
    let pathname = url.pathname
    let fullpath = hostname + pathname
    if (fullpath.length > 0 && fullpath.slice(-1) === '/'){
        fullpath = fullpath.slice(0, -1)
    }
    return fullpath
}


const isValidUrl = urlString => {
    try {
        return Boolean(new URL(urlString));
    } catch (e) {
        return false;
    }
}

function getURLsFromHTML(htmlBody, baseURL) {
    let links = []
    const doc = new JSDOM(htmlBody)
    const anchors = doc.window.document.querySelectorAll('a')
    for (let index = 0; index < anchors.length; index++) {
        let link = anchors[index].href
        //handle relative urls
        if (link.startsWith('/')) {
            link = baseURL + link
            links.push(link);
            continue
        }
        //handle absolute urls
        if (link.endsWith('/')) {
            link = link.slice(0, -1)
        }
        //handle faulty url
        if (isValidUrl(link)) {
            links.push(link);
        }
    }
    return links
};

async function crawlPage(baseUrl) {
   try {
        const response = await fetch(baseUrl)
        if (response.status >= 400 || !response.headers.get("content-type").includes("text/html")) {
            throw new Error("a fail status code or unexpected type.")
        } else {
            //html text
            let body = await response.text()
            return body
        }
   } catch (error) {
       console.error(error)
       return
   }
}


//crawlPage();
//steps
//1. currentURL and baseURL runs on the same domain
//  --ex. wagslane.com have the same domain wagslane.com:8000/path
//2. call normalizeURL() of currentURL
//  -- normalizeURL("wagslane.dev:8000/path") --> wagslane.dev/path
//3. if that normalized url is present in the pages object,
    //then increment 'count'(maybe {...'wagslane.dev/path' = x+1;...}) in pages object and return pages object
//  -- if 'wagslane.dev/path' in pages, then pages['wagslane.dev/path']++; return pages;
//4. else if that normalized url is not present, then add it to pages with value set to 1;
//     --NOTE: if the currentURL is the baseURL set it to 0 in the pages object.
//5. call fetch() to currentURL then store to a variable; add some console.log(`crawling in ${currentURL}`)
//     --EDIT: this part calls fetch from crawlPage() itself. See line:5
//6. call getURLsFromHTML() store to a variable, use crawlPage's output OR the 'body' variable
//     --NOTE: the call on fetch() here is only for the unexistent url (from step 4)
//7. call crawlPage() recursively from the the output of getURLsFromHTML() (which is an array)
//8. return the pages object
//
    //function exports:
//    normalizeURL,
//    getURLsFromHTML, <-- accepts (htmlBody, baseURL)
//    crawlPage, <-- returns html text; accepts (baseURL)


module.exports = {
    normalizeURL,
    getURLsFromHTML,
    crawlPage,
}
