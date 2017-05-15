var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';

var mydbInit = (db,cb) =>{
  db.collection('players').insertOne({
    'name':'kobe',
    'age':18,
    'position':'guard'
  }, (err,result) =>{
    assert.equal(err,null);
    console.log('Insert a docunent in plyers done!');
    cb();
  });
};




MongoClient.connect(url, (err ,db) =>{
  assert.equal(null,err);
  console.log('Connected correctly to server!');

  mydbInit(db,() =>{
    console.log('Init ok!!');
    db.close();
  });

  findDB(db,()=>{
    db.close();
  });
});
