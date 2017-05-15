var fs = require('fs');
var dir = 'file.md';


fs.readFile(dir, 'UTF-8', function(err, data){
  if(err){
    console.error(err);
  } else {
    console.log(data);
  }
})
