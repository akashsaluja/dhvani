export function getDataInshorts() {
    return Promise(function(resolve, reject) {
        var request = require('request');
        var htmlparser = require('htmlparser');
        var newsItem = require('./news');
        var newsItems = [];
        var bodyPending = false;
        var headlinePending = false;
        var latestNewsItem = null;
        request('https://www.inshorts.com/en/read', function (error, response, body) {
            var parser = new htmlparser.Parser({
                onopentag: function(name, attribs){
                    if(name === "span" && attribs.itemprop === "datePublished"){
                        latestNewsItem.timestamp = attribs.content;
                        newsItems.push(latestNewsItem);
                    } else if(name === "div" && attribs.itemprop === "articlebody"){
                        bodyPending = true;
                    } else if(name === "span" && attribs.itemprop === "headline") {
                        headlinePending = true;
                    }
                },
                ontext: function(text){
                    if(bodyPending == true && latestNewsItem != null) {
                        latestNewsItem.text = text;
                        bodyPending = false;
                    } else if(headlinePending == true) {
                        latestNewsItem = newsItem.News(text, null, null);
                        headlinePending = false;
                    }
                },
                onend: function() {
                    resolve(newsItems);
                }
            }, {decodeEntities: true});
            parser.write(body);
            parser.end();
        });
    });
}