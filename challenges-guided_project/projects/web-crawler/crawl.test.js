const { test, expect } = require('@jest/globals');
const { normalizeURL } = require('./crawl.js');

test('normalizing url protocol', () => {
        expect(normalizeURL('https://example.com/path/to/file')).toBe('example.com/path/to/file')
});

test('normalizing url port', () => {
        expect(normalizeURL('https://example.com:8080/path')).toBe('example.com/path')
});

test('normalizing url capitals', () => {
        expect(normalizeURL('https://EXAMPLE.com:8080/path/')).toBe('example.com/path')
});

test('normalizing url http', () => {
        expect(normalizeURL('http://example.com:8080/path/')).toBe('example.com/path')
});
