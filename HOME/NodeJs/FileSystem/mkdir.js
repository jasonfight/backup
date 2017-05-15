var fs = require('fs');
// var re = fs.exists('./hello');
// console.log(re);
// if (re) {
//
//   console.log('1111');
// }

fs.exists('./hello',function(exists){
  if (exists) {
     fs.rmdir('./hello');
     console.log('文件存在.已经删除');
  }else{
    fs.mkdirSync('./hello')
  }
});
