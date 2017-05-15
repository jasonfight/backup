var express = require('express');
var router = express.Router();

var mongoose = require('../database');

/* GET home page. */

router.get('/', function(req, res, next) {

  mongoose.find({},function(err,data){
    console.log(data,'=======');

    // var info = {title:data.标题,
    //   text:data.内容};

      res.render('index', { info: data });
  });


});


router.post('/',function(req,res,next){
  var data = {title:req.body.title,
              text:req.body.text};

mongoose.save(data,function(err){
  if (err) console.log(err);
});

  console.log(data);

  res.render('index',{title:'todo~~',data:[data]})
});

module.exports = router;
