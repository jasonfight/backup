var file = require('fs');
var data = 'hello world NNNN  ';
try{
  file.writeFileSync('22.md',data,'utf-8');
} catch(err){
  console.log(err);
}
