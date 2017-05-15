var file = require('fs');

file.exists('./22.md',function(exists){
  console.error(exists?'file is exists':'file is not found')
});
console.log('this is test');
// NOTE: out:
// this is test
// file is exists
