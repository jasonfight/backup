var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';

function Insert(db,collection,data,cb){
  db.collection(collection).insert(data);
  cb();
};


MongoClient.connect(url, (err,db) =>{
  assert.equal(null,err);
  console.log('Connected correctly to server!');

  var data = {
    name:'guohao',
    age:26,
    position:'center'
  };
  var collection = 'players';

  Insert(db,collection,data,function(){
    console.log('Insert ok!!');
    db.close();
  });
});
