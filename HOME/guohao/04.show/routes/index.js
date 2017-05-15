var express = require('express');
var router = express.Router();
var db = require('../database')
/* GET home page. */
var id;
router.get('/', function(req, res, next) {
  db.User.findOne(function(err,data){
    data.gender='male'?'男':"女";
    res.render('index', {data:data});
    id = data._id;
  })
});


router.post('/update',function(req,res){
    console.log('-------------------',id);

    db.User.update({_id:id},{$set:req.body},function(err,data){
      if (err) console.log(err);
      console.log('保存成功');
      req.body.gender='male'?'男':"女";
      res.render('index', {data:req.body});
    });

})





module.exports = router;
