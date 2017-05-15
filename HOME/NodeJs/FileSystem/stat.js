var fs = require('fs');
fs.stat('./22.md',function(err,stats){
  if (err) {
    console.log('can not find file');
  }else{
    console.log(stats);
  }
})
