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
var schema = new Schema({
  name:    String,
  binary:  Buffer,
  living:  Boolean,
  updated: { type: Date, default: Date.now },
  age:     { type: Number, min: 18, max: 65 },
  mixed:   Schema.Types.Mixed,
  _someId: Schema.Types.ObjectId,
  array:      [],
  ofString:   [String],
  ofNumber:   [Number],
  ofDate:    [Date],
  ofBuffer:   [Buffer],
  ofBoolean:  [Boolean],
  ofMixed:    [Schema.Types.Mixed],
  ofObjectId: [Schema.Types.ObjectId],
  nested: {
    stuff: { type: String, lowercase: true, trim: true }
  }

});



var Thing = mongoose.model('Thing', schema);

var m = new Thing;


m.name = 'Statue of Liberty'
m.age = 50;
m.updated = new Date;
m.binary = new Buffer(0);
m.living = false;
m.mixed = { any: { thing: 'i want' } };
m.markModified('mixed');
m._someId = new mongoose.Types.ObjectId;
m.array.push(1);
m.ofString.push("strings!");
m.ofNumber.unshift(1,2,3,4);
m.ofBuffer.pop();
m.ofMixed = [1, [], 'three', { four: 5 }];
m.nested.stuff = 'good';

m.ofDate.addToSet(new Date);


m.save(function(err,data){
  if (err) console.log(err);
  console.log(data);
});
