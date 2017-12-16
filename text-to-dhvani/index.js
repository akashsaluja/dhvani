module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    context.res = {
        status: 200
        body: 'Hey AKash'
    }
    // if (req.query.name || (req.body && req.body.name)) {
    //     context.log('Came here 1');
    //     request('http://www.bing.com', function (error, response, body) {
    //     // This callback function will never be called
    //         if (err) {
    //             context.log(err);
    //         }

    //         if (!error && response.statusCode == 200) {
    //             context.log(body) // Show the HTML for the Bing homepage. 
    //         }
    //         context.done();
    //     });
    // }
    // else {
    //     context.log('Came here 2');
    //     context.res = {
    //         status: 400,
    //         body: "Please pass a name on the query string or in the request body"
    //     };
    // }
    context.done();
};
