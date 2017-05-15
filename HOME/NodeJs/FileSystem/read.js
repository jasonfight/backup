var fs = require('./myreadFile.js')

fs.myreadFile('ceshi.md','utf8',function(err,data){
	console.log(data);
});
