var express = require('express');
var router = express.Router();
var db = require('../database')

var bcrypt = require('bcrypt');
const salt = 10;

var app = express();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/register',function(req,res,next){
  res.render('register');
});




router.get('/test',function(req,res){
  console.log('req.query.account');
  db.User.findOne({account:req.query.account},function(err,data){
    console.log(data);
    if (!data) {
      res.json('ok')
    }else{
      res.json('notok')
    }
  })
})

router.get('/login',function(req,res,next){
  res.render('login',{message:req.session.messages})
});

router.post('/login',function(req,res){
  console.log(req.body);
  var account = req.body.account;
  var password = req.body.password;

      db.User.findOne({account:account},function(err,data){
      console.log(account);

      if (data){
        bcrypt.compare(password,data.password,function(err,hash){
                  if(hash){
                    console.log('req.session:',req.session);
                    // req.session.user = account;
                    req.session.user = account;
                    res.redirect('/');
                  }else{
                    req.session.messages = '密码错误,请重新输入';
                    res.redirect('/login');
                  }
          });
      }else{
          req.session.messages = '账号不存在';
          res.redirect('login');
      }
});
});


router.post('/register',function(req,res){
  console.log(req.body);
  var user = new db.User(req.body);
  console.log(req.body);
  // console.log(user); //可能是数据库中的字段名
  bcrypt.hash(req.body.password,salt,function(err,hash){
    console.log(hash);
    user.password = hash;
    user.save(function(err){
      console.log('数据存储成功');
      res.redirect('/login');
    });
  });
});






module.exports = router;
