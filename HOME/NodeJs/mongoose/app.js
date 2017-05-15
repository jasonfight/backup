var mongoose = require('mongoose');//// NOTE: 引入mongoose模块
var url = 'mongodb://127.0.0.1:27017/stu'; // NOTE: 指定mongo数据库地址

mongoose.connect(url);  //// NOTE: 连接数据库

var db = mongoose.connection;//// NOTE: 生成数据库句柄

db.on('error',function(error){  // NOTE: 注册error事件,数据库连接不成功时发出提示
  console.log(error);
  console.log('数据库连接错误');
});

db.once('open',function(){   // NOTE: 注册单次open事件,数据连接成功时发出提示.
    console.log('数据库连接成功');
});

// 创建Schema
var Schema = mongoose.Schema  // NOTE: 创建Schema(计划),用来定义数据集合的格式

var userSchema = new Schema({  // NOTE: 使用Schema创建数据的格式
  name:String,
  age:Number,
  date:Date,
  alive:Boolean
});

//创建模板,该模板的名称为数据库集合的名称, userSchema为数据格式.
var User = mongoose.model('User',userSchema);

//创建数据

var jason = new User({
  name:'Jason',
  age:25,
  date:'02/21/1992',
  alive:true
});



jason.save(function(err,data){
  if (err) {
    console.log(err);
  }else{
    console.log(data);
  }
});

//查找数据
User.findOne({},function(err,data){
  console.log(data);
});

//

// User.findOne({},function(err,data){
//   if(err) console.log(err);
//   console.log(data);
//   db.close();
// })
