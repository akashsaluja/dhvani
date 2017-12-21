var request = require('request');
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    if (req.query.name || (req.body && req.body.name)) {
        var request = require('request');
        context.log('Came here 2');
        request('http://www.google.com', function (error, response, body) {
            context.log('Came here 3');
            response.setEncoding('utf8');
            context.log('Came here 5');
            context.res = {
                    status: 200,
                    body: body
            };
            context.bindings.outputQueueItem = "Name passed to the function: " + 
            (req.query.name || req.body.name);
            context.done();
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
