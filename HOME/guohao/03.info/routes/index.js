var express = require('express');
var router = express.Router();
var db = require('../database')
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

router.post('/info',function(req,res){
    var user = new db.User(req.body);
    console.log(req.body);
    user.save(function(err){
      if (err) concole.log(err)
      res.redirect('/')
    })
})
module.exports = router;
