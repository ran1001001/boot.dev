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

module.exports = {
    normalizeURL
}
