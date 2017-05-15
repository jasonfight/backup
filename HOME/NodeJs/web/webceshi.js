var http = require('http');

var file = require('fs');
var query = require('querystring')

var serv = http.createServer(function(req,res,data){
  if (req.url === '/') {
    res.writeHead(200,{'Content-Type':'text/html'});
    file.readFile('form.html','utf8',function(err,data){

      if (err) res.end('404! can not find pages!');
        res.end(data);
    });
  }else if(req.url === '/abc' && req.method ==='POST'){

    req.on('data',(chunk) => {
      var info = query.parse(chunk.toString());
  	  console.log(info);
      data = JSON.stringify(info);
      console.log(data);
  	  file.writeFile('hello.html',data,'utf8',(err) => {
    		if (err) console.log(err);
      });
    });
    req.on('end',() => {
      res.writeHead(200,{'Content-Type':'text/html'});

      file.readFile('hello.html','utf8', (err,data2) => {
        if (err) res.end('error! 404!!!!!');
        info2 = JSON.parse(data2);

        for (var i in info2) {
          res.write('<h1>'+i+':'+info2[i]+'</h2>');
        };

      res.end();
      });
  });
};
});
serv.listen(3000);
