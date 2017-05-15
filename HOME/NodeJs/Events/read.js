var fs = require('fs')
fs.readFile('file.md','UTF-8',function(err,data){
  if (err) {
    console.error(err);
  }else{
    console.log(data);
  }
});
console.log('read file finished...');
