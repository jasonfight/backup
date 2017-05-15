var http = require('http')
var ser = http.createServer(function(req,res){
	res.writeHead(200,{'Content-Type':'text/html'});
	res.end('<h1> Hi Welcome to NodeJs');
});
ser.listen(8000)
