var file = require('fs');
var data = 'hello world';
var fileName = process.argv[2] //从终端读取第一个参数值.
file.writeFile(fileName,data,'utf-8',function(err){
  if (err) {
    console.log(err);
  }
});
