
var http = require('http');
var fs = require('fs');
var serv = http.createServer((req,res) => {
  if (req.url == '/'){
  res.writeHead(200,{'Content-Type':'text/html'});
  fs.readFile('form.html','utf8',(err,data) =>{
    if (err) res.end('404! can not find files');
     res.end(data);
  });
}else if(req.url =='/url'  && req.method == 'POST'){
    var name = '';
    req.on('data',(chunk) => {
      console.log(chunk.toString());
      var info = query.parse(chunk.toString());
      name += info.name;
      password += info.passwd
    });

    req.on('end',() => {
      res.writeHead(200,{'Content-Type':'text/html'});
      res.end(['Your sent a <em>' + req.method + '</em> request',
        '<p>Data: ' + name + '</p>'].join(' '));
    });
}else{
  res.writeHead(404,{'Content-Type':'text/html'});
  res.end('<h1>ERROR 404!!!! can not find the page ~~</h1>')
}
});
serv.listen(3000);
