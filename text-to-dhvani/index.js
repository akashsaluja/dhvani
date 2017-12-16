module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    if (req.query.name || (req.body && req.body.name)) {
        context.log('Came here 1');
        const myRequest = new Request('http://www.bing.com', {method: 'GET'});
        fetch(myRequest).
        then(response => {
            context.res = {
                status: 200,
                body: response
            };
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
