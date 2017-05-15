const EventEmitter = require('events');
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('发生了一个事件！');
});
if(myEmitter.emit('event1')){
  console.log('have a event');
}else {
  console.log('not have a event');
}

myEmitter.on('error', (err) => {
  console.log(err);
});


//myEmitter.emit('error', new Error('whoops!'));

setTimeout(() => {
  myEmitter.emit('event');
}, 3000);
