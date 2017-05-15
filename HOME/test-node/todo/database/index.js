var mongoose = require('mongoose');

var url = 'mongodb://127.0.0.1:27017/todo';

mongoose.connect(url);

var db = mongoose.connection;

db.once('open',function(){
  console.log('数据库连接成功');
});

var Schema = mongoose.Schema;

var todoSchema = new Schema({
  标题:String,
  内容:String
});


var Todo = mongoose.model('Todo',todoSchema);

module.exports = Todo;
