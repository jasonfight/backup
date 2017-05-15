var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';
var data;
var collection;

function Insert(db,collection,data,cb){
  db.collection(collection).insert(data);
  cb();
};


module.exports.insert=function(data){
  console.log(data);
  MongoClient.connect(url,function(err,db){
    assert.equal(err,null);
    Insert(db,collection,data,function(){
      db.close()
    });
  });
}
