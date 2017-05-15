var express = require('express');
var router = express.Router();

var db = require('../database'); // NOTE:


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
  db.findOne({},function(err,data){
    console.log(data);
  })


});

module.exports = router;
