var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = 'mongodb://127.0.0.1:27017/stu';


var findDB = (db,option,callback) => {
      var cursor = db.collection('players').find(option);
      callback(cursor);
}



MongoClient.connect(url, (err ,db) =>{
  assert.equal(null,err);
  console.log('Connected correctly to server!');

  findDB(db,{'age':36},(docs)=>{
      docs.each((err,doc)=>{
        assert.equal(err,null);
        if (doc !== null) {
          console.log(doc)
        }else{
        console.log('show db ok ');
        db.close();
      }
      })
  });
});
