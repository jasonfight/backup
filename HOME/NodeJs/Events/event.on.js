var EventEmitter = require('events').EventEmitter  //引入事件库

var event = new EventEmitter();// 实例化一个对象

event.on('some_event',function(){   // 绑定一个自定义事件
  console.log('some event occured');
});

setTimeout(function(){
  event.emit('some_event');    // 执行事件
},2000);
