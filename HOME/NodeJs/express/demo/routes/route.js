
module.exports = function(app){
  var bodyParser = require('body-parser');

  app.use(bodyParser.json({limit: '1mb'}));  //body-parser 解析json格式数据
  app.use(bodyParser.urlencoded({            //此项必须在 bodyParser.json 下面,为参数编码
    extended: true
  }));

  var info = [{name:'zhangsan',age:30,email:'zhangsan@11.com'},
              {name:'lisi',age:20,email:'lisi@11.com'},
            {name:'wangwu',age:22,email:'wangwu@11.com'}];

  //使用模板,render:将模板"index.ejs",发送给前端.
  app.get('/', function (req, res){
  	res.render('index', {info:info});
  });
  // app.get('/',(req,res)=>{
  //   res.send('welcome to Node.js');
  // });


  app.get('/info',(req,res)=>{
    res.send('Show infomation');
  });

  app.get('/admin',(req,res) =>{
    res.send('Admin page');
  })

//url中正则表达式的使用
  app.get('/ab*cd',(req,res)=>{
    res.send('ab*cd');
  });

// 处理采用get方式提交.
  app.get('/get',(req,res)=>{
    console.log(req.query.getname);
    res.send('get ok');
  });

//处理采用post方式提交.
  app.post('/post',(req,res)=>{
    console.log(req.body.name);
    res.send('post ok');
  });
}
