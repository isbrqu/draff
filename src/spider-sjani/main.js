const cheerio = require('cheerio');
const fs = require('fs-extra');
const got = require('got');
const writeStream = fs.createWriteStream('quote.csv');

async function init() {
    const url = 'https://quotes.toscrape.com';
    const response = await got(url);
    const $ = cheerio.load(response.body);
    writeStream.write('quote,author,tags\n');
    $('.quote').each((index, element) => {
        const quote = $(element);
        const obj = {
            quote: quote.find('.text').text().replace(/(^\“|\”$)/g, ''),
            author: quote.find('.author').text(),
            tags: '',
        };
        obj.tags = quote.find('a.tag').map((index, element) => {
            return $(element).text();
        }).toArray().join(',');
        writeStream.write(`"${obj.quote}","${obj.author}","${obj.tags}"\n`);
    });
}

init()

