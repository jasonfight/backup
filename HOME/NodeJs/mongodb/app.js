var  http = require('http');
var fs = require('fs');
var query = require('querystring');
var mongodb = require('./db');

var all;
var a = http.createServer(function(req, res){
  if('/' === req.url){
    res.writeHead(200, {'Content-Type': 'text/html'});
    fs.readFile('./web.html', function(err, file){
      if(err){
        res.write('Error for 404!');
        res.end('');
      }else{
        res.write(file);
        res.end();
      }
    });
  } else if('/url' === req.url && 'POST' === req.method){
    var name = '';
    req.on('data', function(chunk){
        name += chunk;
        all = query.parse(name);
    });
    req.on('end', function(){

      mongodb.insert('players',all);

      res.writeHead(200, {'Content-Type': 'text/html' });
      res.write("Title:" + all.title);
      res.write("<hr />");
      res.write("Content:" + all.content);
      res.end();
    });
  }else if('/info' === req.url){
    res.writeHead(200, {'Content-Type': 'text/html'});

    mongodb.find({}, function(docs){

        docs.each(function(err, doc){
          if(doc !== null){
            res.write("Title:" + doc.title);
            res.write("<br />");
            res.write("content:" + doc.content);
            res.write("<hr />");
          } else {
            res.end();
          }
        });
    });


  }else {
    res.writeHead(404, {'Content-Type': 'text/html'});
    res.end('<h1> 404 error</h1>')

  }

});

a.listen(3000);
console.log('server: localhost:3000');
