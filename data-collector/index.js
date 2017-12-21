var request = require('request');
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    if (req.query.name || (req.body && req.body.name)) {
        context.log('Came here 1');
        request('http://www.bing.com', function (error, response, body) {
            response.setEncoding('utf8');
            response.on('data', function (chunk) {
                context.res = {
                    status: 200,
                    body: JSON.stringify(chunk)
                };
                context.log('Came here 4');
                context.done();
            });
        });
    }
    else {
        context.log('Came here 2');
        context.res = {
            status: 400,
            body: "Please pass a name on the query string or in the request body"
        };
        context.done();
    }
    
};
