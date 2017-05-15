var express = require('express');
var app = express();
//制定路由文件
var routes = require('./routes/route.js')(app);
//指定模板解析引擎.
app.set('view engine', 'ejs');
//指定模板文件
app.set('views', __dirname+'/views');
app.listen(3000);
