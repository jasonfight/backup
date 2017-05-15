var mongoose = require('mongoose');
var url = 'mongodb://127.0.0.1:27017/exam_info';
mongoose.connect(url);

var db = mongoose.connection;

db.once('open',function(){
  console.log('数据库连接成功');
});


var Schema = mongoose.Schema;

var userSchema= new Schema({
  name:String,
  gender:String,
  age:Number,
  email:String,
  birthday:Date,
});

module.exports.User = mongoose.model('User',userSchema);