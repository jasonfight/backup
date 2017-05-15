var mongoose = require('mongoose');

var url = 'mongodb://127.0.0.1:27017/users';

mongoose.connect(url);
var db = mongoose.connection;

db.once('open',function(){
  console.log('数据库连接成功!');
});

var Schema = mongoose.Schema;

var userSchema = new Schema({
  name:String,
  age:Number,
  date:Date,
  alive:Boolean
});

var Hello = mongoose.model('Hello',userSchema);


Hello.findOne({},function(err,data){
  console.log(data);
  db.close();
});



module.exports = Hello;
