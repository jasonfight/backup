var http = require('http');
var fs = require('fs')
var serv = http.createServer(function(req, res,data){
    if (req.url === '/') {
      res.writeHead(200,{'Content-Type':'text/html'})
      fs.readFile('index.html','utf-8',function(err,data){
        if (err) {
          res.end('404,page not find')
        }else{
          res.end(data)
        }
      })
    }
});
serv.listen(3000);
