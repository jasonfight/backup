var express = require('express');
var app = express();

var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var index = require('./routes/index');
var users = require('./routes/users');

var http = require('http').Server(app);
var io = require('socket.io')(http);


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// app.use('/users', users);
var router = express.Router();

//所有事件都卸载connection中,事件名称不能重复
// io.on('connection',function(socket){

//在首页中进行socket.io通讯

  // socket.on('index_req',function(data){
  //   socket.emit('index_res','index_res 发送成功');
  //   console.log(data);
  // });

app.use(function(req,res,next){
  req.nihao = 'hehehehehe';
  next();
});

app.use('/', index);




//在hello 页面中进行io通讯
  // socket.on('hello_req',function(data){
  //     console.log(data);
  //     socket.emit('hello_res','hello_res发送成功')
  // });
// });



// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});


http.listen(3000,function(){
  console.log('监听端口3000');
})
