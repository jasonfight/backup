var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';

//定义更新函数并进行封装
function deletedb(db,option,callback){
  var cursor = db.collection('one').remove(option);
  callback();
}

MongoClient.connect(url, function(err,db){
  assert.equal(err,null);
  console.log(err); //null
  console.log('Connected correctly to server!');

  // 调用函数

  deletedb(db,{'name':'paul'},()=>{
    if (err) {
      console.log(err);
    }else{
      console.log('delete ok');
      db.close();
    };
  });
});
