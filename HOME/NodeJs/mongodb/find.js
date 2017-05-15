var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var fs = require('fs')

var url = 'mongodb://127.0.0.1:27017/stu';
var collection = 'players'
var data = {'age':36};

var findDB = (db,collection,option,callback) => {
      var cursor = db.collection(collection).find(option);
      callback(cursor);
};

MongoClient.connect(url, (err ,db) =>{

  assert.equal(null,err);
  console.log('Connected correctly to server!');

  findDB(db,collection,data,(cursor)=>{
      cursor.each((err,doc)=>{
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
