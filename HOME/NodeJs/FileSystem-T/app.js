var http = require('http');

var ser = http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('<h1>Hello world!</h1>');
});

ser.listen(3000);
console.log("http://localhost:3000");
