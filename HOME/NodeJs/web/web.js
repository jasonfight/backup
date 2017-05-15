var http = require('http');

var file = require('fs');
var query = require('querystring')
var text;

var serv = http.createServer(function(req,res,data){
  if (req.url === '/') {
    res.writeHead(200,{'Content-Type':'text/html'});
    file.readFile('form.html','utf8',function(err,data){
      // console.log(data);
      if (err) {
        res.end('404! can not find pages!');
      }else{
        res.end(data);
      }
  });
  }else if(req.url === '/abc' && req.method ==='POST'){
    var name = '';
    var password = '';
    req.on('data',(chunk) => {
      var info = query.parse(chunk.toString());
  	  console.log(info);
      data = JSON.stringify(info);
      console.log(data);
  	  file.writeFile('hello.html',data,'utf8',(err) =>{
    		if (err) console.log(err);
      });
      name += info.name
      password += info.passwd;
      if (name == '') {
          res.end('<h1> Please input a name</h1>')
        }
    });
    req.on('end',() => {
      res.writeHead(200,{'Content-Type':'text/html'});
      res.end(['Your sent a <em>' + req.method + '</em> request',
    '<p> Data:' + name + '</p>'+'<p>Password:'+password+'</p>'].join(' '));
  });
}else if(req.url = '/info'){
  file.readFile('hello.html','utf8', (err,data2) => {
    if (err) res.end('error! 404!!!!!');
    info2 = JSON.parse(data2);

    for (var i in info2) {
      res.write('<h1>'+i+':'+info2[i]+'</h2>');
    }
  })

}
});
serv.listen(3000);
