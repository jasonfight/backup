var file = require('fs');
file.readFile('123.md',function(err,data){
  console.log(data);
});
console.log('读取信息');
