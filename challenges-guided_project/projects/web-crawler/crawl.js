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

module.exports = {
    normalizeURL,
    getURLsFromHTML
}
