var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var value = 0;
app.get('/', function(req, res){
  res.sendFile(__dirname + '/半成品.html');
});

io.on('connection', function(socket){
  value +=1;
  //触发广播事件:
  socket.broadcast.emit('broadcast','hello');

  //触发socket事件:
  io.sockets.emit('socket',{num:value})

  /*
  chat:监听的事件名称
  msg:页面传过来的第二参数.{msg:$('#m').val(),name:$('#name').val()}
  callback,页面传过来的第三餐宿.
  */

  socket.on('chat',function(msg,callback){
    console.log(msg);
    io.emit('message',msg);
    callback('ok');
  });
});


http.listen(3000, function(){
  console.log('listening on:3000');
});
