var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';

//定义更新函数并进行封装
var updatedb = (db,option,content,callback) =>{
  var cursor = db.collection('one').updateOne(option,content);
  console.log(cursor);
  callback(cursor);

}

MongoClient.connect(url, (err ,db) =>{
  assert.equal(null,err);
  console.log('Connected correctly to server!');


  // 调用函数
  updatedb(db,{'name':'Guohao'},{$set:{'name':'jason','age':25}},()=>{
  // updatedb(db,{'name':'jason'},{$set:{'name':'Guohao','age':25}},()=>{
    if (err) {
      console.log(err);
    }else{
      console.log('update ok');
      db.close();
  };
  });
});
