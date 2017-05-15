var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var  value = 0;

app.get('/',function(req,res){
  res.sendFile( __dirname + '/ceshi.html');
});
io.on('connection',function(socket){
  value += 1;
  socket.on('name',function(msg,callback){
    io.emit('message',msg);
    callback('ok');
  });
});

http.listen(3000,function(){
  console.log('listening on:3000');
})
