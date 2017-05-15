var fs = require('fs');

var data = fs.readFileSync('file.md', 'UTF-8');
console.log(data);
console.log("read file the end!");
