var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';

function Insert(db,collection,data,cb){
  db.collection(collection).insert(data);
  cb();
};

  var data = {
    name:'guohao',
    age:26,
    position:'center'
  };
  var collection = 'players';


module.export.insert  = function(data){
  console.log(data);
  MongoClient.connect(url,function(err,db){
    assert.equal(err,null);
    Insert(db,data,function(){
      db.close()
    });
  });
}
